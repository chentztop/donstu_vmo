


alphabet = input("Введите список символов (алфавит): ")
summa = 0

# Подсчет количества символов в алфавите
alphabet_count = len(alphabet)
print(f"Количество символов в алфавите: {alphabet_count}")
if alphabet_count > 2 :
    # Проверяем наличие повторяющихся символов в алфавите
    if len(alphabet) != len(set(alphabet)):
        print("В алфавите есть повторяющиеся символы. Пожалуйста, введите уникальные символы.")
    else:
        word = input("Введите слово для проверки: ")

        letter_positions = []

        for letter in word:
            if letter in alphabet:
                position = alphabet.index(letter) + 1
                letter_positions.append(position)
            else:
                print(f"Буква '{letter}' не найдена в алфавите.")

        print("Номера букв в алфавите:")
        print(letter_positions)

        # Подсчет количества букв в слове
        letter_count = len(word)
        print(f"Количество букв в слове: {letter_count}")

    positions_letter = letter_positions[::-1]

    for i in range(letter_count):
        formula = (int(alphabet_count) ** i) * positions_letter[i]
        summa += formula
        if i < letter_count-1:
            print(f"{alphabet_count}^{i} * {letter_positions[i]}+")
        else:
            print(f"{alphabet_count}^{i} * {letter_positions[i]} = ")


    print(f"{summa}")

else:
    print("В  алфавите не достаточно символов")

