"""
    Помехоустойчивое Кодирование Хэмминга


"""



import random

import pickle
import copy
import logging
import math

BinaryStr = str
Index = int
IsKeyBlock = bool



def binary_to_word(binary_str):
    if not binary_str:
        return "" # Возвращаем пустую строку, если входная строка пуста

    # Разделение двоичного числа на группы по 8 бит
    binary_chunks = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]

    # Преобразование каждой группы в символ и объединение в слово
    word = ''.join(chr(int(chunk, 2)) for chunk in binary_chunks)

    return word

def save_to_file(value, filename):
    with open(filename, 'wb') as file:
        pickle.dump(value, file)

def load_from_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


# Функция для изменения случайного символа в двоичной записи числа
def change_random_bit(binary_str):
    if binary_str is None:
        print("Ошибка: переменная binary_str не инициализирована.")
        return

    position = random.randint(0, len(binary_str) - 1)
    new_bit = '0' if binary_str[position] == '1' else '1'
    binary_str = binary_str[:position] + new_bit + binary_str[position + 1:]

    print(f"Изменен символ на позиции {position + 1} на {new_bit}")
    return binary_str


def word_to_binary(word):
    # Проверка длины слов
    # Преобразование каждой буквы в двоичное число и объединение в одно число
    binary_number = ''.join(format(ord(char), '08b') for char in word)

    return binary_number


def encode(to_encode: BinaryStr) -> BinaryStr:
    """
        Кодирование данных по алгоритму Хэмминга

        :param to_encode: Двоичная строка для кодирования

        :return: Закодированная двоичная строка

        :raises ValueError: Если входные данные не в двоичном формате
    """

    if not all(bit in '01' for bit in to_encode):
        raise ValueError('Входные данные должны быть в двоичном формате')

    data: dict[Index, tuple[int, IsKeyBlock]] = {}
    to_encode_iter = iter(to_encode)

    # Первичное заполнение
    index = 1
    while True:
        is_key_block = math.log2(index).is_integer()
        bit = None
        if not is_key_block and not (bit := next(to_encode_iter, None)):
            break
        data[index] = (0 if is_key_block else int(bit), is_key_block)
        index += 1

    # Матрица преобразований
    transformation_matrix: list[list[int]] = [
        [0 for __ in data.keys()]
        for _ in filter(lambda x: x[1], data.values())
    ]
    for index in data.keys():
        bin_value_iter_reversed = reversed(bin(index)[2:])
        for i in range(len(transformation_matrix)):
            if bit := next(bin_value_iter_reversed, None):
                transformation_matrix[i][index - 1] = int(bit)
                continue
            break

    # Расчет ключевых блоков
    codeword: list[int] = [el[0] for el in data.values()]
    for i, row in enumerate(transformation_matrix):
        data[2 ** i] = (sum(map(lambda x: x[0] * x[1], zip(codeword, row))) % 2, True)

    logging.info(
        f'Матрица преобразований: \n{" \t".join(str(value) for value in data.keys())}\n'
        f'{"-\t" * (len(data))}\n'
        f'{" \t".join(str(el) for el in codeword)}\n'
        f'{"-\t" * (len(data))}\n'
        f'{"\n".join(
            " \t".join(str(el) for el in row) + f" \tr{i} = [{data[2 ** i][0]}]"
            for i, row in enumerate(transformation_matrix)
        )}\n'
    )
    return ''.join(str(value[0]) for index, value in data.items())


def decode(to_decode: BinaryStr, max_repair_repeat: int = 10):
    """
        Декодирование данных по алгоритму Хэмминга

        :param to_decode: Двоичная строка для декодирования
        :param max_repair_repeat: Максимальное количество повторов восстановления данных

        :return: Декодированная двоичная строка

        :raises ValueError: Если входные данные не в двоичном формате
        :raises ValueError: Если количество повторов меньше 1
    """

    if not all(bit in '01' for bit in to_decode):
        raise ValueError('Входные данные должны быть в двоичном формате')

    if max_repair_repeat < 1:
        raise ValueError('Количество повторов должно быть больше 0')

    data: dict[Index, tuple[int, IsKeyBlock]] = {
        index: (int(value), math.log2(index).is_integer())
        for index, value in enumerate(to_decode, 1)
    }

    # Матрица преобразований
    transformation_matrix: list[list[int]] = [
        [0 for __ in data.keys()]
        for _ in filter(lambda x: x[1][1], data.items())
    ]
    for index in data.keys():
        bin_value_iter_reversed = reversed(bin(index)[2:])
        for i in range(len(transformation_matrix)):
            if bit := next(bin_value_iter_reversed, None):
                transformation_matrix[i][index - 1] = int(bit)
                continue
            break

    # Восстановление данных
    temp_data = copy.deepcopy(data)
    for attempt_num in range(max_repair_repeat):
        for index in map(lambda x: x[0], filter(lambda x: x[1][1], temp_data.items())):
            temp_data[index] = (0, True)

        codeword = [el[0] for el in temp_data.values()]
        for i, row in enumerate(transformation_matrix):
            temp_data[2 ** i] = (sum(map(lambda x: x[0] * x[1], zip(codeword, row))) % 2, True)

        doesnt_match = list(filter(lambda x: x[1][0] != data[x[0]][0] and x[1][1] and data[x[0]][1], temp_data.items()))
        logging.info(
            f'[{attempt_num}] Матрица синдромов: \n'
            f'{" \t".join(str(value) for value in temp_data.keys())}\n'
            f'{"-\t" * (len(temp_data))}\n'
            f'{" \t".join(str(el) for el in codeword)}\n'
            f'{"-\t" * (len(temp_data))}\n'
            f'{"\n".join(
                " \t".join(str(el) for el in row) + f" \tr{i} = [{temp_data[2 ** i][0]}]"
                for i, row in enumerate(transformation_matrix)
            )}'
        )
        if not doesnt_match:
            logging.info(f'Декодирование завершено')
            break

        dm_bit_index = sum(map(lambda x: x[0], doesnt_match))
        logging.info(
            f'Кажется, не совпадает бит под номером {dm_bit_index!r}\n'
            f'Пробую заменить [{temp_data[dm_bit_index][0]}] на [{int(not temp_data[dm_bit_index][0])}]\n'
        )
        bad_elem = temp_data[dm_bit_index]
        if bad_elem[1]:
            data[dm_bit_index] = (int(not data[dm_bit_index][0]), True)
        temp_data[dm_bit_index] = (int(not temp_data[dm_bit_index][0]), temp_data[dm_bit_index][1])

    return ''.join(str(value[0]) for index, value in temp_data.items() if not value[1])


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s - %(message)s'
    )
    data = ""
    encoded = encode
    # encoded = "01101111001011111"
    decoded = decode(encoded)
    print(decoded)
    print("decoded: ", decoded == data)