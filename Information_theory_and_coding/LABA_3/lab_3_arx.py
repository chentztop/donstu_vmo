from itertools import islice


def chunks(iterable, size):
    iterator = iter(iterable)
    while chunk := list(islice(iterator, size)):
        yield chunk


DEGREE_BIT_MASK_REVERSE = {
    0: 0b11111111,
    1: 0b11111110,
    2: 0b11111100,
    3: 0b11111000,
    4: 0b11110000,
    5: 0b11100000,
    6: 0b11000000,
    7: 0b10000000,
    8: 0b00000000,
}  # 2 ** (8 - i) - 1
import os


from PIL import Image
from PIL.PyAccess import PyAccess

PathLike = str | os.PathLike


def hide(cover_path: PathLike, img_path: PathLike, output_dir: PathLike, degree_count: int) -> PathLike:
    if not (1 <= degree_count <= 8):
        raise ValueError("Степень должна быть от [1, 8]")

    container = Image.open(cover_path)
    data = Image.open(img_path)

    if container.format != "BMP":
        raise ValueError("Ошибка: Контейнер должен быть формата BMP")

    if data.format != "BMP":
        raise ValueError("Ошибка: Данные для скрытия должны быть формата BMP")

    container_pixels: PyAccess = container.load()
    data_pixels: PyAccess = data.load()

    result_path = os.path.join(output_dir, f"hidden_{degree_count}.bmp")

    data_byte_count = data.size[0] * data.size[1] * 3
    container_byte_count = (container.size[0] * container.size[1] * 3 * degree_count) // 8
    if data_byte_count > container_byte_count:
        raise ValueError(
            f"Размер данных для скрытия больше размера контейнера "
            f"{data_byte_count=} vs {container_byte_count=}"
        )

    chunked_data_bits = chunks(
        (
            bit
            for i in range(data.size[0])
            for j in range(data.size[1])
            for value in data_pixels[i, j]
            for bit in format(value, '08b')
        ),
        degree_count
    )
    for i in reversed(range(container.height)):
        for j in range(container.width):
            container_pixel = list(container_pixels[j, i])

            for channel in range(3):
                data_bits = next(chunked_data_bits, None)
                if data_bits is None:
                    break

                if len(data_bits) < degree_count:
                    data_bits += "0" * (degree_count - len(data_bits))

                container_pixel[channel] = (
                        container_pixel[channel] &
                        DEGREE_BIT_MASK_REVERSE[degree_count] +
                        int(f"0b{''.join(data_bits)}", 2)
                )
            container_pixels[j, i] = tuple(container_pixel)

    container.save(result_path, format="BMP")
    return result_path


def reveal(img_path: str, output_dir: str, degree_count: int) -> str:
    if not (1 <= degree_count <= 8):
        raise ValueError("Степень должна быть от [1, 8]")

    img = Image.open(img_path)
    img_pixels: PyAccess = img.load()

    if img.format!= "BMP":
        raise ValueError("Ошибка: изображение должно быть типа BMP")

    reveal_path = os.path.join(output_dir, f"revealed_{degree_count}sl.bmp")
    buffer = []
    for i in reversed(range(img.height)):
        for j in range(img.width):
            img_pixel = list(img_pixels[j, i])

            for channel in range(3):
                buffer.append(format(img_pixel[channel], '08b')[-degree_count:])

    data_bits = (bit for bit in ''.join(buffer))
    data_bytes_iter = iter((int(''.join(bits), 2) for bits in chunks(data_bits, 8)))
    for i in reversed(range(img.height)):
        for j in range(img.width):
            img_pixel = list(img_pixels[j, i])

            for channel in range(3):
                color_byte = next(data_bytes_iter, None)
                if color_byte is None:
                    break
                img_pixel[channel] = color_byte
            img_pixels[j, i] = tuple(img_pixel)

    img.save(reveal_path, format="BMP")
    return reveal_path



def request_int(request_text: str = "\n\nВведите число") -> int | None:
    print(request_text)
    value = input("Ввод: ")
    if not value.isdigit():
        print("Значение не является числом")
        return None
    return int(value)


def request_filepath(request_text: str = "\n\nВведите путь к файлу") -> str | None:
    print(request_text)
    filepath = input("Путь: ")
    if not os.path.exists(filepath):
        print("Файл не найден")
        return
    return filepath


def encode_file():
    pass


def decode_file():
    pass


def hide_image():
    filepath_cover = request_filepath("\n\nВведите путь к изображению-контейнеру [BMP]")
    filepath_img = request_filepath("Введите путь к изображению, которое нужно спрятать [BMP]")
    degree_count = request_int("Введите степень записи:")
    output_dir = os.path.dirname(filepath_img)

    result_path = hide(
        cover_path=filepath_cover,
        img_path=filepath_img,
        output_dir=output_dir,
        degree_count=degree_count
    )
    print("Файл успешно спрятан")
    print("Результат сохранен в файл: ", result_path)


def reveal_image():
    filepath_img = request_filepath("\n\nВведите путь к изображению, которое нужно раскрыть")
    degree_count = request_int("Введите степень записи:")
    output_dir = os.path.dirname(filepath_img)

    if not (1 <= degree_count <= 8):
        print("Ошибка: Степень должна быть от [1, 8]")
        return

    result_path = reveal(img_path=filepath_img, output_dir=output_dir, degree_count=degree_count)
    print("Файл успешно раскрыт")
    print("Результат сохранен в файл: ", result_path)


def main():
    while True:
        print("\n\nЧто вы хотите сделать?")
        print("1. Закодировать изображение")
        print("2. Раскодировать изображение")
        print("5. Выход")
        choice = input("Ваш выбор: ")
        if choice == "1":
            encode_file()
        elif choice == "2":
            decode_file()
        elif choice == "5":
            break
        else:
            print("Неверный ввод")


if __name__ == "__main__":
    main()



















