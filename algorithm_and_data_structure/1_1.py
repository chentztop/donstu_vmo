A = set()


def add_element_to_set(element):
    A.add(element)

def print_set():
    print("Множество A содержит следующие элементы:")
    for idx, element in enumerate(A):
        print(f"Элемент {idx+1}: {element}")
    print(f"Всего элементов в множестве A: {len(A)}")


def print_set_B():
    print("Множество B содержит следующие элементы:")
    for idx, element in enumerate(A):
        print(f"Элемент {idx+1}: {element}")
    print(f"Всего элементов в множестве B: {len(A)}")


while True:
    print('1. Задание-1')
    print('2. Задание_2')
    print('3. Задание_3')
    print('4. Задание_4')
    print('4. Задание_5')

    выбор = input('Выберите пункт меню: ')
    if выбор == '1':
        A = set()
        add_element_to_set(1)
        add_element_to_set(2)
        add_element_to_set(3)
        add_element_to_set(4)
        add_element_to_set(5)
        print_set()

    if выбор == '2':
        A = set()
        add_element_to_set(4)
        add_element_to_set(5)
        add_element_to_set(6)

        print_set_B()

    if выбор == '3':

        sentence1 = input('Выберите предложение_1: ')
        sentence2 = input('Выберите предложение_2: ')

        # Разбиваем предложения на слова
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Создаем множества из слов
        set1 = set(words1)
        set2 = set(words2)

        # Находим общие слова
        common_words = []
        for word in set1:
            if word in set2:
                common_words.append(word)

        print("Общие слова в двух предложениях:")
        for common_word in common_words:
            print(common_word)

    if выбор == '4':

        S = input("Введите множество символов: ")


        russian_alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        latin_alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        digits = set('0123456789')


        G = set()
        F = set()
        C = set()


        for char in S:
            if char in russian_alphabet:
                G.add(char)
            elif char in latin_alphabet:
                F.add(char)
            elif char in digits:
                C.add(char)

        print("Подмножество А (русские буквы):", G)
        print("Подмножество Б (латинские буквы):", F)
        print("Подмножество В (цифры):", C)

    if выбор == '5':

        S = input("Введите множество символов: ")

        russian_alphabet = set('бвгджзйклмнпрстфхцчшщъь')
        latin_alphabet = set('уеёаояиюэы')

        G = set()
        F = set()

        for char in S:
            if char in russian_alphabet:
                G.add(char)
            elif char in latin_alphabet:
                F.add(char)


        print("Подмножество А (русские буквы):", G)
        print("Подмножество Б (латинские буквы):", F)







