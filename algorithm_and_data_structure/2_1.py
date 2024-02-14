import random
import re





while True:
    print('1. Задание-1')
    print('2. Задание_2')
    print('3. Задание_3')
    print('4. Задание_4')
    print('4. Задание_5')

    выбор = input('Выберите пункт меню: ')
    if выбор == '1':
        filename = "numbers.txt"
        with open(filename, "w") as file:
            for _ in range(10):
                number = random.uniform(-10, 10)  # Генерируем случайное действительное число от -10 до 10
                file.write(str(number) + "\n")

        # Открываем файл для чтения и определяем количество отрицательных чисел
        negative_count = 0
        with open(filename, "r") as file:
            for line in file:
                number = float(line.strip())
                if number < 0:
                    negative_count += 1

        print(f"Количество отрицательных чисел в файле {filename}: {negative_count}")

    if выбор == '2':
        def insert_letter(filename, position, letter):
            with open(filename, "r") as file:
                data = file.read()

            if position < 0:
                position = 0
            elif position > len(data):
                position = len(data)

            new_data = data[:position] + letter + data[position:]

            with open(filename, "w") as file:
                file.write(new_data)


        # Пример использования
        filename = "text_2"
        insert_letter(filename, 5, "X")

    if выбор == '3':
        def print_nth_line(filename, n):
            with open(filename, "r") as file:
                lines = file.readlines()

            if 1 <= n <= len(lines):
                print(f"{n}-я строка текста: {lines[n - 1]}")
            else:
                print(f"В файле нет {n}-й строки.")


        # Пример использования
        print_nth_line("text_3", 2)
        print_nth_line("text_3", 4)

    if выбор == '4':
        def find_substring_in_file(filename, substring):
            results = []  # Список для хранения результатов поиска

            with open(filename, "r") as file:
                lines = file.readlines()

            for line_num, line in enumerate(lines, start=1):
                pos = 0
                while pos < len(line):
                    found_pos = line.find(substring, pos)
                    if found_pos == -1:
                        break
                    results.append((line_num, found_pos + 1))
                    pos = found_pos + 1

            return results


        # Пример использования
        filename = "text_3"
        substring = "строка"
        search_results = find_substring_in_file(filename, substring)

        if search_results:
            for line_num, char_num in search_results:
                print(f"Подстрока найдена в строке {line_num}, позиция {char_num}")
        else:
            print("Подстрока не найдена в файле.")

    if выбор == '5':
        def count_unique_words_in_file(filename):
            unique_words = set()

            with open(filename, "r") as file:
                text = file.read()
                words = re.findall(r'\b\w+\b', text)  # Находим все слова в тексте

                for word in words:
                    unique_words.add(word.lower())  # Приводим слово к нижнему регистру для уникальности

            return len(unique_words)


        def count_word_occurrences_in_file(filename):
            word_occurrences = {}

            with open(filename, "r") as file:
                text = file.read()
                words = re.findall(r'\b\w+\b', text)  # Находим все слова в тексте

                for word in words:
                    word = word.lower()  # Приводим слово к нижнему регистру
                    if word in word_occurrences:
                        word_occurrences[word] += 1
                    else:
                        word_occurrences[word] = 1

            return word_occurrences


        # Пример использования
        filename = "text_3"

        unique_word_count = count_unique_words_in_file(filename)
        print(f"Количество уникальных слов в файле: {unique_word_count}")

        word_occurrences = count_word_occurrences_in_file(filename)
        for word, count in word_occurrences.items():
            print(f"Слово '{word}' встречается {count} раз(а) в файле.")







