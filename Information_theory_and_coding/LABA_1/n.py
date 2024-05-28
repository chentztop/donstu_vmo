from collections import Counter, defaultdict
import heapq

class ShannonFanoNode:
    def __init__(self, symbol=None, freq=0):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def shannon_fano_coding(symbols_with_freq):
    def split_symbols(symbols):
        total = sum([sym[1] for sym in symbols])
        acc = 0
        for i, sym in enumerate(symbols):
            acc += sym[1]
            if acc >= total / 2:
                return symbols[:i+1], symbols[i+1:]

    def build_tree(symbols):
        if len(symbols) == 1:
            return ShannonFanoNode(symbols[0][0], symbols[0][1])
        left_symbols, right_symbols = split_symbols(symbols)
        node = ShannonFanoNode()
        node.left = build_tree(left_symbols)
        node.right = build_tree(right_symbols)
        node.freq = node.left.freq + node.right.freq
        return node

    def generate_codes(node, prefix="", codebook={}):
        if node is None:
            return
        if node.symbol is not None:
            codebook[node.symbol] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
        return codebook

    sorted_symbols = sorted(symbols_with_freq.items(), key=lambda x: -x[1])
    root = build_tree(sorted_symbols)
    codebook = generate_codes(root)
    return codebook

def compress_shannon_fano(data):
    frequency = Counter(data)
    codebook = shannon_fano_coding(frequency)
    encoded_data = ''.join([codebook[symbol] for symbol in data])
    return codebook, encoded_data

def decompress_shannon_fano(codebook, encoded_data):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded_data = ""
    buffer = ""
    for bit in encoded_data:
        buffer += bit
        if buffer in reverse_codebook:
            decoded_data += reverse_codebook[buffer]
            buffer = ""
    return decoded_data

# Example usage
data = "this is an example for shannon fano compression"
codebook, compressed_data = compress_shannon_fano(data)
print("Compressed data:", compressed_data)
decompressed_data = decompress_shannon_fano(codebook, compressed_data)
print("Decompressed data:", decompressed_data)
def compress_lzss(data, window_size=4096, lookahead_buffer_size=18):
    i = 0
    output = []
    while i < len(data):
        match = (-1, 0)
        for j in range(max(0, i - window_size), i):
            length = 0
            while length < lookahead_buffer_size and i + length < len(data) and data[j + length] == data[i + length]:
                length += 1
            if length > match[1]:
                match = (i - j, length)
        if match[1] > 2:
            output.append((match[0], match[1]))
            i += match[1]
        else:
            output.append(data[i])
            i += 1
    return output

def decompress_lzss(compressed_data, window_size=4096):
    i = 0
    output = []
    while i < len(compressed_data):
        if isinstance(compressed_data[i], tuple):
            (offset, length) = compressed_data[i]
            for j in range(length):
                output.append(output[-offset])
            i += 1
        else:
            output.append(compressed_data[i])
            i += 1
    return ''.join(output)

# Example usage
data = "this is an example for lzss compression"
compressed_data = compress_lzss(data)
print("Compressed data:", compressed_data)
decompressed_data = decompress_lzss(compressed_data)
print("Decompressed data:", decompressed_data)
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def compress_file(input_filename, output_filename, algorithm):
    data = read_file(input_filename)
    if algorithm == "shannon_fano":
        codebook, compressed_data = compress_shannon_fano(data)
        write_file(output_filename, f"{codebook}\n{compressed_data}")
    elif algorithm == "lzss":
        compressed_data = compress_lzss(data)
        write_file(output_filename, str(compressed_data))

def decompress_file(input_filename, output_filename, algorithm):
    data = read_file(input_filename)
    if algorithm == "shannon_fano":
        codebook_str, compressed_data = data.split('\n', 1)
        codebook = eval(codebook_str)
        decompressed_data = decompress_shannon_fano(codebook, compressed_data)
    elif algorithm == "lzss":
        compressed_data = eval(data)
        decompressed_data = decompress_lzss(compressed_data)
    write_file(output_filename, decompressed_data)

# Example usage
input_file = "mumu (1).txt"
compressed_file_sf = "compressed_sf.txt"
decompressed_file_sf = "decompressed_sf.txt"
compressed_file_lzss = "compressed_lzss.txt"
decompressed_file_lzss = "decompressed_lzss.txt"

# Compress and decompress using Shannon-Fano
compress_file(input_file, compressed_file_sf, "shannon_fano")
decompress_file(compressed_file_sf, decompressed_file_sf, "shannon_fano")

# Compress and decompress using LZSS
compress_file(input_file, compressed_file_lzss, "lzss")
decompress_file(compressed_file_lzss, decompressed_file_lzss, "lzss")
