def generate_words(alphabet, length, current_word, words_dict, next_key):
    if length == 0:
        words_dict[next_key] = current_word
        return next_key + 1
    for char in alphabet:
        next_key = generate_words(alphabet, length - 1, current_word + char, words_dict, next_key)
    return next_key

alphabet = ["0", "1"]
max_length = 10

all_words_dict = {}
next_key = 1
for l in range(1, max_length + 1):
    next_key = generate_words(alphabet, l, "", all_words_dict, next_key)

while True:
    print('1. Вывести весь универсум')
    print('2. Вывести все элементы по 1 задачи')
    print('3. Вывести все элементы по 2 задачи')

 
    выбор = input('Выберите пункт меню: ')
    if выбор == '1':

        for key, value in all_words_dict.items():
            print(f"Лексикографический номер: : {key}, Слово: {value}")
    if выбор == '2':
        for key, value in all_words_dict.items():
            if value.endswith("11") and "00" in value:
                print(f"Лексикографический номер: {key}, Слово: {value}")

    if выбор == '3':
        for key, value in all_words_dict.items():
            if value.count("000") == 1 and "0000" not in value:
                print(f"Лексикографический номер: : {key}, Слово: {value}")

