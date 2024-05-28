"""Интерфейс к библиотеке сжатия liblzma.

Этот модуль предоставляет класс для чтения и записи сжатых файлов,
классы для инкрементного сжатия (de) и удобные функции для
однократного сжатия (de).

Эти классы и функции поддерживают как форматы контейнеров XZ, так и устаревшие
форматы контейнеров LZMA, а также необработанные сжатые потоки данных.
"""

__all__ = [
    "CHECK_NONE", "CHECK_CRC32", "CHECK_CRC64", "CHECK_SHA256",
    "CHECK_ID_MAX", "CHECK_UNKNOWN",
    "FILTER_LZMA1", "FILTER_LZMA2", "FILTER_DELTA", "FILTER_X86", "FILTER_IA64",
    "FILTER_ARM", "FILTER_ARMTHUMB", "FILTER_POWERPC", "FILTER_SPARC",
    "FORMAT_AUTO", "FORMAT_XZ", "FORMAT_ALONE", "FORMAT_RAW",
    "MF_HC3", "MF_HC4", "MF_BT2", "MF_BT3", "MF_BT4",
    "MODE_FAST", "MODE_NORMAL", "PRESET_DEFAULT", "PRESET_EXTREME",

    "LZMACompressor", "LZMADecompressor", "LZMAFile", "LZMAError",
    "open", "compress", "decompress", "is_check_supported",
]

import builtins
import io
import os
from _lzma import *
from _lzma import _encode_filter_properties, _decode_filter_properties
import _compression

_MODE_CLOSED = 0
_MODE_READ = 1
# Value 2 no longer used
_MODE_WRITE = 3


class LZMAFile(_compression.BaseStream):
    """Файловый объект, обеспечивающий прозрачное сжатие LZMA (de).

     LZMAFile может выступать в качестве оболочки для существующего файлового объекта или
    ссылаться непосредственно на именованный файл на диске.

     Обратите внимание, что LZMAFile предоставляет интерфейс *двоичного* файла - считанные данные
    возвращаются в виде байтов, а данные для записи должны быть указаны в виде байтов.
     """

    def __init__(self, filename=None, mode="r", *,
                 format=None, check=-1, preset=None, filters=None):
        """Откройте файл, сжатый с помощью LZMA, в двоичном режиме.

         имя файла может быть либо фактическим именем файла (заданным в виде строки,
        байтов или объекта, подобного пути), и в этом случае открывается именованный файл
        , либо это может быть существующий файловый объект для чтения или
        записи.

         режим может быть "r" для чтения (по умолчанию), "w" для записи (поверх),
        "x" для создания исключительно или "a" для добавления. Они могут
        быть эквивалентно указаны как "rb", "wb", "xb" и "ab" соответственно.

         формат определяет формат контейнера, который будет использоваться для файла.
         Если режим "r", по умолчанию используется FORMAT_AUTO. В противном случае значение по
        умолчанию равно FORMAT_XZ.

         check указывает используемую проверку целостности. Этот аргумент можно
        использовать только при открытии файла для записи. Для FORMAT_XZ
        значение по умолчанию равно CHECK_CRC64. FORMAT_ALONE и FORMAT_RAW не
        поддерживают проверку целостности - для этих форматов параметр check должен быть
        опущен или иметь значение CHECK_NONE.

         При открытии файла f
        """
        self._fp = None
        self._closefp = False
        self._mode = _MODE_CLOSED

        if mode in ("r", "rb"):
            if check != -1:
                raise ValueError("Не удается указать проверку целостности "
                                 "при открытии файла для чтения")
            if preset is not None:
                raise ValueError("Не удается указать предустановленное сжатие "
                                 "уровень при открытии файла для чтения")
            if format is None:
                format = FORMAT_AUTO
            mode_code = _MODE_READ
        elif mode in ("w", "wb", "a", "ab", "x", "xb"):
            if format is None:
                format = FORMAT_XZ
            mode_code = _MODE_WRITE
            self._compressor = LZMACompressor(format=format, check=check,
                                              preset=preset, filters=filters)
            self._pos = 0
        else:
            raise ValueError("Invalid mode: {!r}".format(mode))

        if isinstance(filename, (str, bytes, os.PathLike)):
            if "b" not in mode:
                mode += "b"
            self._fp = builtins.open(filename, mode)
            self._closefp = True
            self._mode = mode_code
        elif hasattr(filename, "read") or hasattr(filename, "write"):
            self._fp = filename
            self._mode = mode_code
        else:
            raise TypeError("filename must be a str, bytes, file or PathLike object")

        if self._mode == _MODE_READ:
            raw = _compression.DecompressReader(self._fp, LZMADecompressor,
                                                trailing_error=LZMAError, format=format, filters=filters)
            self._buffer = io.BufferedReader(raw)

    def close(self):
        """Очистите и закройте файл.

         Может вызываться более одного раза без ошибок. Как только файл будет
        закрыт, любая другая операция с ним вызовет ValueError.
         """
        if self._mode == _MODE_CLOSED:
            return
        try:
            if self._mode == _MODE_READ:
                self._buffer.close()
                self._buffer = None
            elif self._mode == _MODE_WRITE:
                self._fp.write(self._compressor.flush())
                self._compressor = None
        finally:
            try:
                if self._closefp:
                    self._fp.close()
            finally:
                self._fp = None
                self._closefp = False
                self._mode = _MODE_CLOSED

    @property
    def closed(self):
        """Значение True, если этот файл закрыт.."""
        return self._mode == _MODE_CLOSED

    def fileno(self):
        """Возвращает файловый дескриптор для базового файла."""
        self._check_not_closed()
        return self._fp.fileno()

    def seekable(self):
        """Возвращает, поддерживает ли файл поиск."""
        return self.readable() and self._buffer.seekable()

    def readable(self):
        """Return whether the file was opened for reading."""
        self._check_not_closed()
        return self._mode == _MODE_READ

    def writable(self):
        """Возвращает, был ли файл открыт для чтения."""
        self._check_not_closed()
        return self._mode == _MODE_WRITE

    def peek(self, size=-1):
        """Возвращает буферизованные данные без продвижения позиции файла.

         Всегда возвращает по крайней мере один байт данных, если не указано значение EOF.
         Точное количество возвращаемых байт не указано.
         """
        self._check_can_read()
        # Relies on the undocumented fact that BufferedReader.peek() always
        # returns at least one byte (except at EOF)
        return self._buffer.peek(size)

    def read(self, size=-1):
        """Считывает из файла несжатые байты до размера.

         Если размер отрицательный или пропущен, считывает до тех пор, пока не будет достигнут EOF.
         Возвращает b"", если файл уже находится в EOF.
         """
        self._check_can_read()
        return self._buffer.read(size)

    def read1(self, size=-1):
        """Считывает данные до размера несжатых байт, стараясь избежать
        многократного чтения из базового потока. Считывает данные до
        размера буфера, если размер отрицательный.

         Возвращает b"", если файл находится в EOF.
         """
        self._check_can_read()
        if size < 0:
            size = io.DEFAULT_BUFFER_SIZE
        return self._buffer.read1(size)

    def readline(self, size=-1):
        """Считывает строку несжатых байтов из файла.

         Завершающая новая строка (если присутствует) сохраняется. Если размер
        неотрицателен, будет прочитано не более байтов размера (в этом
        случае строка может быть неполной). Возвращает b", если уже находится в EOF.
         """
        self._check_can_read()
        return self._buffer.readline(size)

    def write(self, data):
        """Записать объект bytes в файл.

         Возвращает количество записанных несжатых байтов, которое
        всегда является длиной данных в байтах. Обратите внимание, что из-за буферизации
        файл на диске может не отражать записанные данные до тех пор, пока не будет вызвана функция close()
         .
         """
        self._check_can_write()
        if isinstance(data, (bytes, bytearray)):
            length = len(data)
        else:
            # accept any data that supports the buffer protocol
            data = memoryview(data)
            length = data.nbytes

        compressed = self._compressor.compress(data)
        self._fp.write(compressed)
        self._pos += length
        return length

    def seek(self, offset, whence=io.SEEK_SET):
        """Измените положение файла.

         Новое положение задается смещением относительно
        положения, указанного в where. Возможные значения для where следующие:

         0: начало потока (по умолчанию): смещение не должно быть отрицательным
         1: текущее положение потока
         2: конец потока; смещение не должно быть положительным

         Возвращает новую позицию файла.

         Обратите внимание, что поиск эмулируется, поэтому в зависимости от параметров
        эта операция может быть чрезвычайно медленной.
         """
        self._check_can_seek()
        return self._buffer.seek(offset, whence)

    def tell(self):
        """Возвращает текущую позицию файла."""
        self._check_not_closed()
        if self._mode == _MODE_READ:
            return self._buffer.tell()
        return self._pos


def open(filename, mode="rb", *,
         format=None, check=-1, preset=None, filters=None,
         encoding=None, errors=None, newline=None):
    """Откройте файл, сжатый с помощью LZMA, в двоичном или текстовом режиме.

     имя файла может быть либо фактическим именем файла (заданным в виде строки, байтов
    или объекта, подобного пути), и в этом случае открывается именованный файл, либо это
    может быть существующий файловый объект для чтения или записи.

     Аргументом mode может быть "r", "rb" (по умолчанию), "w", "wb", "x", "xbb",
    "a" или "ab" для двоичного режима, или "rt", "wt", "xt" или "at" для текстового
    режима.

     Аргументы format, check, preset и filters определяют параметры
    сжатия, как для LZMACompressor, LZMADecompressor и
     LZMAFile.

     Для двоичного режима эта функция эквивалентна
    конструктору LZMAFile: LZMAFile(имя файла, режим, ...). В этом случае
    не следует указывать кодировку, ошибки и аргументы новой строки.

     Для текстового режима создается объект LZMAFile и переносится в
    io.Экземпляр TextIOWrapper с указанной кодировкой,
    поведением при обработке ошибок и окончаниями строк.

    """
    if "t" in mode:
        if "b" in mode:
            raise ValueError("Invalid mode: %r" % (mode,))
    else:
        if encoding is not None:
            raise ValueError("Argument 'encoding' not supported in binary mode")
        if errors is not None:
            raise ValueError("Argument 'errors' not supported in binary mode")
        if newline is not None:
            raise ValueError("Argument 'newline' not supported in binary mode")

    lz_mode = mode.replace("t", "")
    binary_file = LZMAFile(filename, lz_mode, format=format, check=check,
                           preset=preset, filters=filters)

    if "t" in mode:
        encoding = io.text_encoding(encoding)
        return io.TextIOWrapper(binary_file, encoding, errors, newline)
    else:
        return binary_file


def compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None):
    """Сжать блок данных.

     Обратитесь к строке документации LZMACompressor для описания
    необязательных аргументов *format*, *check*, *preset* и *filters*.

     Для поэтапного сжатия вместо этого используйте LZMACompressor.
     """
    comp = LZMACompressor(format, check, preset, filters)
    return comp.compress(data) + comp.flush()


def decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None):
    """Распакуйте блок данных.

     Обратитесь к строке документации LZMADecompressor для описания
    необязательных аргументов *format*, *check* и *filters*.

     Для инкрементной распаковки вместо этого используйте LZMADecompressor.
     """
    results = []
    while True:
        decomp = LZMADecompressor(format, memlimit, filters)
        try:
            res = decomp.decompress(data)
        except LZMAError:
            if results:
                break  # Leftover data is not a valid LZMA/XZ stream; ignore it.
            else:
                raise  # Error on the first iteration; bail out.
        results.append(res)
        if not decomp.eof:
            raise LZMAError("Compressed data ended before the "
                            "end-of-stream marker was reached")
        data = decomp.unused_data
        if not data:
            break
    return b"".join(results)


def main():
    with open(r"C:\Users\slesa\PycharmProjects\donstu_vmo\Information_theory_and_coding\kak.txt", mode="r") as f:
        data = f.read()
        
        # compressed = compress(data)
        #
        # with open('mumu1.txt', 'wb') as my_file:
        #     my_file.write(compressed)


if __name__ == "__main__":
    main()
