alphabet = input("Введите список символов (алфавит): ")
k = 10000
l = []
letter_positions = []
# Подсчет количества символов в алфавите
alphabet_count = len(alphabet)
print(f"Количество символов в алфавите: {alphabet_count}")
if alphabet_count > 2 :
    # Проверяем наличие повторяющихся символов в алфавите
    if len(alphabet) != len(set(alphabet)):
        print("В алфавите есть повторяющиеся символы. Пожалуйста, введите уникальные символы.")
    else:
        N = int(input("Введите номер слова : "))

        while k >= alphabet_count:

            if N%alphabet_count == 0:
                r = alphabet_count
                k = (N -alphabet_count) // alphabet_count
                N = k
                l.append(r)
                print(k)
                print(r)
            elif N%alphabet_count != 0:
                r = N%alphabet_count
                k = (N - N % alphabet_count) // alphabet_count
                N = k
                print(k)
                print(r)
                l.append(r)
    alphabet = list(alphabet)
    l2 = list(reversed(l))
    for letter in l2:
        position = alphabet[int(letter)-1]
        letter_positions.append(position)
        print(letter_positions)


