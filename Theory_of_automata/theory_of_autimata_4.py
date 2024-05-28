def generate_words(alphabet, length, current_word, words_dict, next_key):
    if length == 0:
        words_dict[next_key] = current_word
        return next_key + 1
    for char in alphabet:
        next_key = generate_words(alphabet, length - 1, current_word + char, words_dict, next_key)
    return next_key


alphabet = ["a", "b"]
max_length = 10

all_words_dict = {}
next_key = 1
for l in range(1, max_length + 1):
    next_key = generate_words(alphabet, l, "", all_words_dict, next_key)

while True:
    print('1. Вывод Юниверсума')
    print('2. Вывод решения')

    выбор = input('Выберите пункт меню: ')
    if выбор == '1':

        for key, value in all_words_dict.items():
            print(f"Лексикографический номер: : {key}, Слово: {value}")

    if выбор == '2':
        for key, value in all_words_dict.items():
            if value.count("bb") == 1 and "bbb" not in value :
                print(f"Лексикографический номер: : {key}, Слово: {value}")

