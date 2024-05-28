import logging

from utils import polynom_bch_table, DICT_POLYNOM_BCH
from src import encode, decode

import random

def word_to_binary(word):
    """
    Преобразует слово в двоичную строку.
    """
    binary_string = ''.join(format(ord(char), '08b') for char in word)
    return binary_string

def binary_to_word(binary_string):
    """
    Преобразует двоичную строку обратно в слово.
    """
    return ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))

def simulate_channel(data, error_rate):
    """
    Эмулирует канал связи с заданной вероятностью ошибки.

    :param data: Исходные данные.
    :param error_rate: Вероятность возникновения ошибки.
    :return: Модифицированные данные с учетом вероятности ошибки.
    """
    modified_data = ""
    for bit in data:
        # Генерируется случайное число от 0 до 1
        error_occurred = random.random() < error_rate
        if error_occurred:
            # Если произошла ошибка, меняется бит
            modified_data += str(int(bit) ^ 1)
        else:
            modified_data += bit
    return modified_data


def encode_dialog():
    print("Выберите порождающий полином:")
    print(polynom_bch_table())
    index = int(input("Введите номер полинома: "))
    polynom = DICT_POLYNOM_BCH[index]
    print(f"Порождающий полином: {polynom[1]} / {polynom[2]}")
    word_to_encode = input(f"\nВведите слово для кодирования: ").strip()
    binary_string = word_to_binary(word_to_encode)
    print(f"Преобразованное в двоичную строку: {binary_string}")
    print(f"Результат кодирования: {encode(binary_string, polynom[2])}\n")


def decode_dialog():
        print("Выберите порождающий полином:")
        print(polynom_bch_table())
        index = int(input("Введите номер полинома: "))
        polynom = DICT_POLYNOM_BCH[index]
        binary_string_to_decode = input(f"\nВведите двоичную строку для декодирования: ").strip()
        error_rate = 0.0
        corrupted_data = simulate_channel(binary_string_to_decode, error_rate)
        print(f"Симулировано канал связи с вероятностью ошибки {error_rate}: {corrupted_data}")
        print(f"Порождающий полином: {polynom[1]} / {polynom[2]}")

        # Эмуляция канала связи с вероятностью ошибки 0.2


        # Декодируем полученную двоичную строку обратно в слово
        decoded_binary_string = decode(corrupted_data, polynom[2], polynom[3][2])
        print(f"Результат декодирования: {decoded_binary_string}")

        decoded_word = binary_to_word(decoded_binary_string)
        print(f"Обратное преобразование в слово: {decoded_word}\n")


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
    )

    print("Что вы хотите сделать?")
    while True:
        print("1. Закодировать")
        print("2. Декодировать")
        print("3. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            encode_dialog()
        elif choice == "2":
            decode_dialog()
        elif choice == "3":
            break
        else:
            print("Неверный ввод")
        print()