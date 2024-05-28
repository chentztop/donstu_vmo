import logging

from  Information_theory_and_coding.LABA_4.utils import (Algor)

import random

import pickle


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




def encode():
    value = input("\n\nВведите слово: ")
    value1 = word_to_binary(value)
    print(value1)
    encoded_value = Algor.encode(value1)
    print("Результат: ", encoded_value)
    return encoded_value



def decode(value):
    try:
        decoded_value = Algor.decode(value)
        print("Результат: ", decoded_value)
        return decoded_value
    except Exception as e:
        print("Ошибка декодирования:", e)
        return "" # Возвращаем пустую строку в случае ошибки


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s - %(message)s'
    )

    print("\n\nЧто вы хотите сделать?")
    print("1. Закодировать последовательность")
    print("3. Выход")
    choice = input("Ваш выбор: ")
    if choice == "1":
        value = encode()
        value_2 = change_random_bit(value)
        save_to_file(value_2, 'value_2.pkl') # Сохранение value_2 в файл
        value_2 = load_from_file('value_2.pkl') # Загрузка value_2 из файла
        v = decode(value_2)
        print(binary_to_word(v))



if __name__ == "__main__":
    main()