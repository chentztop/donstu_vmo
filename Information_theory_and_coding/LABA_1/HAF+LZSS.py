from collections import Counter
import os


class LZSS:
    def __init__(self, window_size, max_length):
        self.window_size = window_size
        self.max_length = max_length

    def compress(self, text):
        compressed_text = ""
        index = 0
        while index < len(text):
            match_found = False
            for length in range(1, min(self.max_length, len(text) - index) + 1):
                window_start = max(0, index - self.window_size)
                candidate = text[index:index + length]

                match_position = window_start + text[window_start:index].rfind(candidate)
                match_length = len(candidate)

                if match_position != index and match_length > 1:
                    compressed_text += f"({index - match_position},{match_length})"
                    index += match_length
                    match_found = True
                    break

            if not match_found:
                compressed_text += text[index]
                index += 1

        return compressed_text

    def decompress(self, compressed_text):
        decompressed_text = ""
        index = 0
        while index < len(compressed_text):
            if compressed_text[index] != '(':
                decompressed_text += compressed_text[index]
                index += 1
            else:
                delimiter_index = compressed_text.find(',', index)
                if delimiter_index == -1:
                    break
                offset = int(compressed_text[index + 1:delimiter_index])

                length_index = compressed_text.find(')', delimiter_index)
                if length_index == -1:
                    break
                length = int(compressed_text[delimiter_index + 1:length_index])

                for i in range(length):
                    if -offset >= 0 and -offset < len(decompressed_text):
                        decompressed_text += decompressed_text[-offset]
                index = length_index + 1

        return decompressed_text


# Функция для сохранения декодированного текста в файл
def save_decompressed_text(text, file_path):
    with open(file_path, 'w', encoding='ANSI') as file:
        file.write(text)
    print(f"Декодированный текст сохранен в файле {file_path}")


class ShannonFanoNode:
    def __init__(self, symbol=None, probability=0):
        self.symbol = symbol
        self.probability = probability
        self.bitstring = ""
        self.left = None
        self.right = None

def calculate_probabilities(file_path):
    try:
        with open(file_path, 'r', encoding='ANSI') as file:
            text = file.read()
            counter = Counter(text)
            total_chars = sum(counter.values())
            probabilities = {char: count / total_chars for char, count in counter.items()}
            return probabilities
    except UnicodeDecodeError:
        print(f"Ошибка декодирования файла {file_path}. Попробуйте использовать другую кодировку.")
        return None




def shannon_fano_coding(symbols, probabilities):
    nodes = [ShannonFanoNode(symbol, probability) for symbol, probability in probabilities.items()]

    def split(nodes):
        if len(nodes) <= 1:
            return

        nodes.sort(key=lambda x: x.probability, reverse=True)

        total_prob = sum(node.probability for node in nodes)
        accumulator = 0
        split_index = 0
        for i, node in enumerate(nodes):
            accumulator += node.probability
            if accumulator >= total_prob / 2:
                split_index = i
                break

        for i in range(len(nodes)):
            if i <= split_index:
                nodes[i].bitstring += "0"
            else:
                nodes[i].bitstring += "1"

        split(nodes[:split_index + 1])
        split(nodes[split_index + 1:])

    split(nodes)

    codes = {node.symbol: node.bitstring for node in nodes}

    return codes

def encode(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text

def decode(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""
    return decoded_text


def save_encoded_text(encoded_text, folder_path, file_name):
    # Создаем папку, если её нет
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Создаем полный путь к файлу сжатого текста
    encoded_file_path = os.path.join(folder_path, file_name)
    # Записываем закодированный текст в файл
    with open(encoded_file_path, 'w', encoding='ANSI') as file:
        file.write(encoded_text)
    print(f"Закодированный текст сохранен в {encoded_file_path}")
    return encoded_file_path

def load_encoded_text(file_path):
    with open(file_path, 'r', encoding='ANSI') as file:
        encoded_text = file.read()
    return encoded_text

# Пример использования
def save_decoded_text(decoded_text, folder_path, file_name):
    # Создаем папку, если её нет
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Создаем полный путь к файлу с декодированным текстом
    decoded_file_path = os.path.join(folder_path, file_name)
    # Записываем декодированный текст в файл
    with open(decoded_file_path, 'w', encoding='ANSI') as file:
        file.write(decoded_text)
    print(f"Декодированный текст сохранен в {decoded_file_path}")
    return decoded_file_path



from collections import Counter
import os


class LZSS:
    def __init__(self, window_size, max_length):
        self.window_size = window_size
        self.max_length = max_length

    def compress(self, text):
        compressed_text = ""
        index = 0
        while index < len(text):
            match_found = False
            for length in range(1, min(self.max_length, len(text) - index) + 1):
                window_start = max(0, index - self.window_size)
                candidate = text[index:index + length]

                match_position = window_start + text[window_start:index].rfind(candidate)
                match_length = len(candidate)

                if match_position != index and match_length > 1:
                    compressed_text += f"({index - match_position},{match_length})"
                    index += match_length
                    match_found = True
                    break

            if not match_found:
                compressed_text += text[index]
                index += 1

        return compressed_text

    def decompress(self, compressed_text):
        decompressed_text = ""
        index = 0
        while index < len(compressed_text):
            if compressed_text[index] != '(':
                decompressed_text += compressed_text[index]
                index += 1
            else:
                delimiter_index = compressed_text.find(',', index)
                if delimiter_index == -1:
                    break
                offset = int(compressed_text[index + 1:delimiter_index])

                length_index = compressed_text.find(')', delimiter_index)
                if length_index == -1:
                    break
                length = int(compressed_text[delimiter_index + 1:length_index])

                for i in range(length):
                    if -offset >= 0 and -offset < len(decompressed_text):
                        decompressed_text += decompressed_text[-offset]
                index = length_index + 1

        return decompressed_text


# Функция для сохранения декодированного текста в файл
def save_decompressed_text(text, file_path):
    with open(file_path, 'w', encoding='ANSI') as file:
        file.write(text)
    print(f"Декодированный текст сохранен в файле {file_path}")


class ShannonFanoNode:
    def __init__(self, symbol=None, probability=0):
        self.symbol = symbol
        self.probability = probability
        self.bitstring = ""
        self.left = None
        self.right = None

import codecs

def calculate_probabilities(file_path):
    try:
        with open(file_path, 'r', encoding='ANSI') as file:
            text = file.read()
            counter = Counter(text)
            total_chars = sum(counter.values())
            probabilities = {char: count / total_chars for char, count in counter.items()}
            return probabilities
    except UnicodeDecodeError:
        print(f"Ошибка декодирования файла {file_path}. Попробуйте использовать другую кодировку.")
        return None




def shannon_fano_coding(symbols, probabilities):
    nodes = [ShannonFanoNode(symbol, probability) for symbol, probability in probabilities.items()]

    def split(nodes):
        if len(nodes) <= 1:
            return

        nodes.sort(key=lambda x: x.probability, reverse=True)

        total_prob = sum(node.probability for node in nodes)
        accumulator = 0
        split_index = 0
        for i, node in enumerate(nodes):
            accumulator += node.probability
            if accumulator >= total_prob / 2:
                split_index = i
                break

        for i in range(len(nodes)):
            if i <= split_index:
                nodes[i].bitstring += "0"
            else:
                nodes[i].bitstring += "1"

        split(nodes[:split_index + 1])
        split(nodes[split_index + 1:])

    split(nodes)

    codes = {node.symbol: node.bitstring for node in nodes}

    return codes

def encode(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text

def decode(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""
    return decoded_text


def save_encoded_text(encoded_text, folder_path, file_name):
    # Создаем папку, если её нет
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Создаем полный путь к файлу сжатого текста
    encoded_file_path = os.path.join(folder_path, file_name)
    # Записываем закодированный текст в файл
    with open(encoded_file_path, 'w', encoding='utf-8') as file:
        file.write(encoded_text)
    print(f"Закодированный текст сохранен в {encoded_file_path}")
    return encoded_file_path

def load_encoded_text(file_path):
    with open(file_path, 'r', encoding='ANSI') as file:
        encoded_text = file.read()
    return encoded_text

# Пример использования
def save_decoded_text(decoded_text, folder_path, file_name):
    # Создаем папку, если её нет
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Создаем полный путь к файлу с декодированным текстом
    decoded_file_path = os.path.join(folder_path, file_name)
    # Записываем декодированный текст в файл
    with open(decoded_file_path, 'w', encoding='ANSI') as file:
        file.write(decoded_text)
    print(f"Декодированный текст сохранен в {decoded_file_path}")
    return decoded_file_path

# Пример использования
file_path = "mumu (1).txt"
probabilities = calculate_probabilities(file_path)
codes = shannon_fano_coding(probabilities.keys(), probabilities)
print("Символы и их коды:", codes)

with open(file_path, 'r', encoding='windows-1251', errors='ignore') as file:
    text = file.read()
    encoded_text = encode(text, codes)
    encoded_file_path = save_encoded_text(encoded_text, "encoded_texts", "encoded_text.txt")
    print("Закодированный текст:", encoded_text)

loaded_encoded_text = load_encoded_text(encoded_file_path)
decoded_text = decode(loaded_encoded_text, codes)
print("Декодированный текст:", decoded_text)

decoded_file_path = save_decoded_text(decoded_text, "decoded_texts", "decoded_text.txt")



file_path = "mumu (1).txt"
probabilities = calculate_probabilities(file_path)
codes = shannon_fano_coding(probabilities.keys(), probabilities)

with open(file_path, 'r', encoding='windows-1251', errors='ignore') as file:
    text = file.read()
    encoded_text = encode(text, codes)

lzss = LZSS(window_size=256, max_length=48)
compressed_text = lzss.compress(encoded_text)

# Сохранение сжатого текста в файл
with open("compressed_text.txt", "w") as file:
    file.write(compressed_text)
print("Сжатый текст сохранен в файле compressed_text.lzss")

decompressed_text = lzss.decompress(compressed_text)

# Сохранение и вывод декодированного текста
save_decompressed_text(decompressed_text, "decompressed_text.txt")

decompressed_text = lzss.decompress(compressed_text)

# Сохранение и вывод декодированного текста
save_decompressed_text(decompressed_text, "decompressed_text.txt")