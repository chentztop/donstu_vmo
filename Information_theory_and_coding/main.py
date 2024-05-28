from PIL import Image
import numpy as np


def hide(container_path, secret_path):
    # Открытие контейнера и секретного изображения
    container_img = Image.open(container_path)
    secret_img = Image.open(secret_path)

    # Преобразование изображений в массивы numpy
    container_array = np.array(container_img)
    secret_array = np.array(secret_img)

    # Получение размеров контейнера
    container_width, container_height = container_array.shape[:2]

    # Проверка, что секретное изображение меньше контейнера
    if secret_array.shape[0] > container_height or secret_array.shape[1] > container_width:
        raise ValueError("Секретное изображение слишком большое для контейнера.")

    # Встраивание секретного изображения в контейнер
    for i in range(secret_array.shape[0]):
        for j in range(secret_array.shape[1]):
            # Изменение младших значащих битов пикселя контейнера
            container_array[i, j] = container_array[i, j] & 0xFE | (secret_array[i, j] & 0x01)

    # Сохранение измененного контейнера
    hidden_img = Image.fromarray(container_array)
    hidden_img.save('hidden_image.bmp')

    return 'hidden_image.png'

container_path = 'white.bmp'
secret_path = 'some.bmp'

hidden_image_path = hide(container_path, secret_path)
print(f"Скрытое изображение сохранено по пути: {hidden_image_path}")
