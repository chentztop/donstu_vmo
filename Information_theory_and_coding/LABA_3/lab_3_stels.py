import os
import base64

BMP_HEADER_SIZE = 54


def encode_image(input_img_name, output_img_name, text: str, degree):
    if degree not in [1, 2, 4, 8]:
        print("Степень записи может быть 1, 2, 4 или 8")
        return False

    input_image = open(input_img_name, "rb")
    output_image = open(output_img_name, "wb")

    bmp_header = input_image.read(BMP_HEADER_SIZE)
    output_image.write(bmp_header)

    text_mask, img_mask = create_masks(degree)

    for symbol in text:
        # in ascii
        symbol = ord(symbol)

        for _ in range(0, 8, degree):
            img_byte = int.from_bytes(input_image.read(1), 'little') & img_mask
            bits = symbol & text_mask
            bits >>= 8 - degree
            # Вставляем бит в байт картинки
            img_byte |= bits

            output_image.write(img_byte.to_bytes(1, 'little'))
            symbol <<= degree

    output_image.write(input_image.read())

    input_image.close()
    output_image.close()

    return True


def decode_image(encoded_img, symbols_to_read, degree):
    if degree not in [1, 2, 4, 8]:
        print("Степень записи может быть 1, 2, 4 или 8")
        return False

    img_len = os.stat(encoded_img).st_size

    if symbols_to_read >= img_len * degree / 8 - BMP_HEADER_SIZE:
        print("Too much symbols to read")
        return False

    encoded_bmp = open(encoded_img, "rb")

    encoded_bmp.seek(BMP_HEADER_SIZE)

    _, img_mask = create_masks(degree)
    img_mask = ~img_mask
    text = ""
    read = 0
    while read < symbols_to_read:
        symbol = 0

        for _ in range(0, 8, degree):
            img_byte = int.from_bytes(encoded_bmp.read(1), 'little') & img_mask
            symbol <<= degree
            symbol |= img_byte

        if chr(symbol) == "\n" and len(os.linesep) == 2:
            read += 1

        read += 1
        text += chr(symbol)

    encoded_bmp.close()
    return text


def create_masks(degree):
    text_mask = 0b11111111
    img_mask = 0b11111111

    text_mask <<= 8 - degree
    text_mask %= 256
    img_mask >>= degree
    img_mask <<= degree

    return text_mask, img_mask


with open("some.bmp", "rb") as file:
    byte_string = file.read()

# переводим в utf-8 string
base64_string = base64.b64encode(byte_string).decode("utf-8")
degree = int(input("Введите степень записи (1, 2, 4, 8)= "))
encode_image("white.bmp", "red.bmp", base64_string, degree)

decoded_byte_string = base64.b64decode(
    decode_image("red.bmp", len(base64_string), degree)
)
with open("hidden_image.bmp", "wb") as bmp_file:
    bmp_file.write(decoded_byte_string)