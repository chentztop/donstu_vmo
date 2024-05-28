import copy
import os
import struct

from PIL import Image

from scr.core.utils import align_to_four_bytes
from scr.core.kaitaibmp import Bmp


def read_bmp_header(file_path):
    with open(file_path, 'rb') as file:
        # Читаем первые 2 байта, которые представляют собой сигнатуру файла (BM)
        file_signature = file.read(2)
        if file_signature != b'BM':
            raise ValueError("Файл не является изображением в формате BMP")
        # Преобразование сигнатуры файла из 16-ричной системы в 10-ричную
        file_signature_decimal = int.from_bytes(file_signature, byteorder='little', signed=False)

        # Читаем размер файла
        file_size = int.from_bytes(file.read(4), byteorder='little')

        # Читаем зарезервированные байты
        reserved_bytes = file.read(4)
        # Преобразование зарезервированных байтов из 16-ричной системы в 10-ричную
        reserved_bytes_decimal = int.from_bytes(reserved_bytes, byteorder='little', signed=False)

        # Читаем смещение данных изображения относительно начала файла
        data_offset = int.from_bytes(file.read(4), byteorder='little')

        # Читаем размер заголовка
        header_size = int.from_bytes(file.read(4), byteorder='little')

        # Читаем ширину и высоту изображения
        width = int.from_bytes(file.read(4), byteorder='little')
        height = int.from_bytes(file.read(4), byteorder='little')

        # Читаем количество плоскостей
        planes = int.from_bytes(file.read(2), byteorder='little')

        # Читаем глубину цвета
        bits_per_pixel = int.from_bytes(file.read(2), byteorder='little')

        # Читаем тип сжатия
        compression_type = int.from_bytes(file.read(4), byteorder='little')

        # Читаем размер изображения в байтах
        image_size = int.from_bytes(file.read(4), byteorder='little')

        # Читаем горизонтальное разрешение
        x_pixels_per_meter = int.from_bytes(file.read(4), byteorder='little')

        # Читаем вертикальное разрешение
        y_pixels_per_meter = int.from_bytes(file.read(4), byteorder='little')

        # Читаем количество цветов в палитре
        colors_used = int.from_bytes(file.read(4), byteorder='little')

        # Читаем важные цвета
        important_colors = int.from_bytes(file.read(4), byteorder='little')

        # Возвращаем словарь с информацией о заголовке
        return {
            'Тип': file_signature_decimal,
            'Размер': file_size,
            'Резерв1': reserved_bytes_decimal,
            'Смещение': data_offset,
            'DIB РАЗМЕР ЗАГОЛОВКА В БАЙТАХ': header_size,
            'Ширина': width,
            'Высота': height,
            'Число плоскостей': planes,
            'Биты пикселей': bits_per_pixel,
            'Тип сжатия': compression_type,
            'image_size': image_size,
            'РАЗМЕР СЖАТОГО ИЗОБРАЖЕНИЯ': x_pixels_per_meter,
            'ВЕРТИКАЛЬНОЕ РАЗРЕШЕНИЕ': y_pixels_per_meter,
            'Количество цветов': colors_used,
            'Количество важных цветов': important_colors
        }



# Пример использования функции


def get_bmp_headers_manually(filepath: str) -> dict[str, any]:
    """Return the header of the BMP file manually."""

    headers = dict()

    with open(filepath, 'rb') as bmp_file:

        # Заголовки файла
        headers["Тип файла"] = bmp_file.read(2).decode("utf-8")
        headers["Размер файла"] = f"{int.from_bytes(bmp_file.read(4), byteorder='little')} байт"
        headers["Зарезервировано 1"] = int.from_bytes(bmp_file.read(2), byteorder='little')
        headers["Зарезервировано 2"] = int.from_bytes(bmp_file.read(2), byteorder='little')
        headers["Смещение до данных"] = f"{int.from_bytes(bmp_file.read(4), byteorder='little')} байт"
        headers[" "] = None

        bmp_type_map = {
            12: "BMP-Core",
            40: "BMP-3",
            52: "BMP-3 [Adobe Photoshop]",
            56: "BMP-3-alpha [Adobe Photoshop]",
            108: "BMP-4",
            124: "BMP-5",
        }

        # Заголовки изображения
        headers["Длина заголовка изображения"] = img_header_size = int.from_bytes(bmp_file.read(4), byteorder='little')
        headers["Тип заголовка изображения"] = bmp_type_map.get(
            img_header_size,
            f"Неизвестный тип (Длина заголовка: {img_header_size} байт)"
        )

        if img_header_size == 12:
            headers["Ширина изображения"] = int.from_bytes(bmp_file.read(2), byteorder='little')
            headers["Высота изображения"] = int.from_bytes(bmp_file.read(2), byteorder='little')
            headers["Плоскости"] = int.from_bytes(bmp_file.read(2), byteorder='little')
            headers["Бит на пиксель"] = int.from_bytes(bmp_file.read(2), byteorder='little')
        else:
            headers["Ширина изображения"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Высота изображения"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Плоскости"] = int.from_bytes(bmp_file.read(2), byteorder='little')
            headers["Бит на пиксель"] = int.from_bytes(bmp_file.read(2), byteorder='little')
            headers["Сжатие"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Размер изображения"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Горизонтальное разрешение"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Вертикальное разрешение"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Количество цветов в палитре"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Количество основных цветов"] = int.from_bytes(bmp_file.read(4), byteorder='little')

        headers["  "] = None

        if img_header_size >= 108:
            headers["Красный канал"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Зеленый канал"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Синий канал"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Альфа канал"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Цветовое пространство"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            bmp_file.read(48)
            headers["   "] = None

        if img_header_size >= 124:
            headers["Предпочтения при рендеринге растра"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Смещение в байтах цветового профиля"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Размер цветового профиля"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["Резерв"] = int.from_bytes(bmp_file.read(4), byteorder='little')
            headers["    "] = None

    return headers


def get_bmp_headers(filepath: str) -> dict[str, any]:
    """Return the header of the BMP file using libraries."""

    headers = dict()

    img = Bmp.from_file(filepath)
    headers["Тип файла"] = img.file_hdr.file_type.decode("utf-8")
    headers["Размер файла"] = f"{img.file_hdr.len_file} байт"
    headers["Зарезервировано 1"] = img.file_hdr.reserved1
    headers["Зарезервировано 2"] = img.file_hdr.reserved2
    headers["Смещение до данных"] = img.file_hdr.ofs_bitmap
    headers[" "] = None

    headers["Длина заголовка изображения"] = img_header_size = img.dib_info.len_header
    headers["Тип заголовка изображения"] = None

    if img_header_size >= 12:
        headers["Ширина изображения"] = img.dib_info.header.image_width
        headers["Высота изображения"] = img.dib_info.header.image_height
        headers["Плоскости"] = img.dib_info.header.num_planes
        headers["Бит на пиксель"] = img.dib_info.header.bits_per_pixel

    if img_header_size >= 40:
        headers["Сжатие"] = img.dib_info.header.bitmap_info_ext.compression
        headers["Размер изображения"] = img.dib_info.header.bitmap_info_ext.len_image
        headers["Горизонтальное разрешение"] = img.dib_info.header.bitmap_info_ext.x_resolution
        headers["Вертикальное разрешение"] = img.dib_info.header.bitmap_info_ext.y_resolution
        headers["Количество цветов в палитре"] = img.dib_info.header.bitmap_info_ext.num_colors_important
        headers["Количество основных цветов"] = img.dib_info.header.bitmap_info_ext.num_colors_used
        headers["  "] = None

    if img_header_size >= 108:
        headers["Красный канал"] = None
        headers["Зеленый канал"] = None
        headers["Синий канал"] = None
        headers["Альфа канал"] = None
        headers["Цветовое пространство"] = img.dib_info.header.bitmap_v4_ext.color_space_type
        headers["   "] = None

    if img_header_size >= 124:
        headers["Предпочтения при рендеринге растра"] = img.dib_info.header.bitmap_v5_ext.intent
        headers["Смещение в байтах цветового профиля"] = img.dib_info.header.bitmap_v5_ext.ofs_profile
        headers["Размер цветового профиля"] = img.dib_info.header.bitmap_v5_ext.len_profile
        headers["Резерв"] = img.dib_info.header.bitmap_v5_ext.reserved
        headers["    "] = None

    return headers


def __set_img_size_header(img_header: bytes, header_len: int, bit_per_pixel: int, img_size: int) -> bytes:
    """Set the size of the image in the header."""
    return (
            struct.pack("<I", header_len) +
            img_header[4:14] +
            struct.pack("<H", bit_per_pixel) +
            img_header[16:20] +
            struct.pack("<I", img_size) +
            img_header[24:40]
    )


def __set_file_size_header(file_header: bytes, file_size: int, offset: int) -> bytes:
    """Set the size of the file in the header."""
    return (
            file_header[:2] +
            struct.pack("<I", file_size) +
            file_header[6:10] +
            struct.pack("<I", offset) +
            file_header[14:]
    )


def color_components_manually(filepath: str) -> list[str]:
    """Return the list of color components of the BMP file (manually)."""
    with open(filepath, "rb") as file:
        # Заголовки
        file_headers = file.read(14)
        offset_to_data = int.from_bytes(file_headers[10:], byteorder='little')

        image_v3_headers = file.read(40)
        file.read(offset_to_data - 54)

        # Чтение размеров изображения
        width = int.from_bytes(image_v3_headers[4:8], byteorder='little')
        height = int.from_bytes(image_v3_headers[8:12], byteorder='little')
        bytes_per_pixel = int.from_bytes(image_v3_headers[14:16], byteorder='little') // 8

        if bytes_per_pixel != 3:
            return ["Невозможно разделить изображение на цветовые компоненты, т.к. оно не в формате RGB"]

        row_size = align_to_four_bytes(width * bytes_per_pixel)

        # Пиксели
        pixels = file.read()

    r_channel = bytearray(copy.copy(pixels))
    g_channel = bytearray(copy.copy(pixels))
    b_channel = bytearray(copy.copy(pixels))

    for row in range(height):

        buffer = list()
        for col in range(1, row_size):
            pixel_index = row * row_size + col
            buffer.append(pixel_index)
            if len(buffer) >= bytes_per_pixel:
                blue_index = buffer[0]
                green_index = buffer[1]
                red_index = buffer[2]

                b_channel[green_index] = 0
                b_channel[red_index] = 0

                g_channel[blue_index] = 0
                g_channel[red_index] = 0

                r_channel[blue_index] = 0
                r_channel[green_index] = 0
                buffer.clear()

    r_file_header = __set_file_size_header(file_headers, len(r_channel) + 54, 54)
    r_headers = r_file_header + __set_img_size_header(image_v3_headers, 40, 24, len(r_channel))

    g_file_header = __set_file_size_header(file_headers, len(g_channel) + 54, 54)
    g_headers = g_file_header + __set_img_size_header(image_v3_headers, 40, 24, len(g_channel))

    b_file_header = __set_file_size_header(file_headers, len(b_channel) + 54, 54)
    b_headers = b_file_header + __set_img_size_header(image_v3_headers, 40, 24, len(b_channel))

    filename = os.path.basename(filepath).replace(".", "_").replace(" ", "_")
    save_dir = os.path.join(os.path.dirname(filepath), f"{filename}_manual_color_components")
    os.makedirs(save_dir, exist_ok=True)

    red_path = os.path.join(save_dir, "RED.bmp")
    green_path = os.path.join(save_dir, "GREEN.bmp")
    blue_path = os.path.join(save_dir, "BLUE.bmp")

    with open(red_path, "wb") as file:
        file.write(r_headers)
        file.write(r_channel)
    with open(green_path, "wb") as file:
        file.write(g_headers)
        file.write(g_channel)
    with open(blue_path, "wb") as file:
        file.write(b_headers)
        file.write(b_channel)

    return [red_path, green_path, blue_path]


def color_components(filepath: str) -> list[str]:
    """Return the list of color components of the BMP file."""

    filename = os.path.basename(filepath).replace(".", "_").replace(" ", "_")
    save_dir = os.path.join(os.path.dirname(filepath), f"{filename}_color_components")
    os.makedirs(save_dir, exist_ok=True)

    output = list()
    with Image.open(filepath) as original_img:

        if original_img.mode != "RGB":
            output.append("Невозможно разделить изображение на цветовые компоненты, т.к. оно не в формате RGB")
            return output

        for color in ["RED", "GREEN", "BLUE"]:
            img = original_img.copy()
            pixels = img.load()
            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    red, green, blue = pixels[i, j]

                    pixels[i, j] = (
                        red if color == "RED" else 0,
                        green if color == "GREEN" else 0,
                        blue if color == "BLUE" else 0,
                    )
            path = os.path.join(save_dir, f"{color}.bmp")
            img.save(path)
            output.append(path)

    return output


def split_image_to_bitplanes_manually(filepath: str) -> list[str]:
    """Return the list of bitplanes of the BMP file (manually)."""

    filename = os.path.basename(filepath).replace(".", "_").replace(" ", "_")
    save_dir = os.path.join(os.path.dirname(filepath), f"{filename}_bit_slices_manually")
    os.makedirs(save_dir, exist_ok=True)

    output = list()
    with Image.open(filepath) as original_img:

        if original_img.mode != "RGB":
            output.append("Невозможно разделить изображение на битплейны, т.к. оно не в формате RGB")
            return output

        for index in range(8):
            img = original_img.copy()
            pixels = img.load()
            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    red, green, blue = pixels[i, j]

                    pixels[i, j] = (
                        255 if red & (1 << index) > 0 else 0,
                        255 if green & (1 << index) > 0 else 0,
                        255 if blue & (1 << index) > 0 else 0,
                    )

            path = os.path.join(save_dir, f"bit_slice_{index}.bmp")
            img.save(path, "BMP")

            output.append(path)

    return output


def split_image_to_bitplanes(filepath: str) -> list[str]:
    """Return the list of bitplanes of the BMP file."""

    filename = os.path.basename(filepath).replace(".", "_").replace(" ", "_")
    save_dir = os.path.join(os.path.dirname(filepath), f"{filename}_bit_slices")
    os.makedirs(save_dir, exist_ok=True)

    with Image.open(filepath) as img:
        output = list()

        if img.mode != "RGB":
            output.append("Невозможно разделить изображение на битплейны, т.к. оно не в формате RGB")
            return output

        for i in range(9):
            bit_slice = img.copy()

            bit_slice = bit_slice.point(lambda p: 255 if p & (1 << i) > 0 else 0)

            path = os.path.join(save_dir, f"bit_slice_{i}.bmp")
            bit_slice.save(path)
            output.append(path)

    return output

def main():
    while True:
        print("\n\nЧто вы хотите сделать?")
        print("1. Прочитать название файла")
        print("2. Разрезать на цвета")
        print("3. Разрезать на битовые срезы")
        print("4. Выход")
        choice = input("Ваш выбор: ")
        if choice == "2":
            image_path = "../Information_theory_and_coding/bmp_24.bmp"

            # Вызов функции
            color_component_files = color_components_manually(image_path)

            # Вывод путей к файлам цветовых компонентов
            for component_file in color_component_files:
                print(f"Файл цветового компонента сохранен по пути: {component_file}")
        elif choice == "3":
            image_path = "red.bmp"

            # Вызов функции
            bitplane_files = split_image_to_bitplanes_manually(image_path)

            # Вывод путей к файлам битпланов
            for bitplane_file in bitplane_files:
                print(f"Файл битплана сохранен по пути: {bitplane_file}")
        elif choice == "1":
            image_path = "some.bmp"
            header_info = read_bmp_header(image_path)
            print(header_info)

            # Вызов функции
        elif choice == "4":
            break
        else:
            print("Неверный ввод")


if __name__ == "__main__":
    main()