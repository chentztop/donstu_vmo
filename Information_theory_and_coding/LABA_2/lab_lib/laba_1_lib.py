
import struct
from PIL import Image
import numpy as np



while True:
    print('1. Задание-1')
    print('2. Заданире_2')
    print('3. Задание_3')

    выбор = input('Выберите пункт меню: ')

    if выбор == '1':
        file = 'hidden_image.bmp'

        with open(file, 'rb') as f:
            # читаем первые 14 байт - заголовок файла
            header = f.read(54)

            # распаковываем заголовок
            b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16 = struct.unpack('<2sIHHIIIIHHIIIIII',
                                                                                                  header)

            # выводим информацию о заголовке
            print('Тип:', b1)
            print('Размер:', b2)
            print('Резерв1:', b3)
            print('Резерв2:', b4)
            print('Смещение:', b5)
            print('DIB РАЗМЕР ЗАГОЛОВКА В БАЙТАХ:', b6)
            print('Ширина:', b7)
            print('Высота:', b8)
            print('ЧИСЛО ПЛОСКОСТЕЙ:', b9)
            print('БИТЫ ПИКСЕЛИ:', b10)
            print('ТИП СЖАТИЯ:', b11)
            print('РАЗМЕР СЖАТОГО ИЗОБРАЖЕНИЯ:', b12)
            print('ГОРИЗОНТАЛЬНОЕ РАЗРЕШЕНИЕ:', b13)
            print('ВЕРТИКАЛЬНОЕ РАЗРЕШЕНИЕ:', b14)
            print('КОЛИЧЕСТВО ЦВЕТОВ:', b15)
            print('КОЛИЧЕСТВО ВАЖНЫХ ЦВЕТОВ:', b16)

    if выбор == '2':
        img = Image.open('hidden_image.bmp')
        data = np.array(img.getdata())

        red = [(d[0], 0, 0) for d in data]
        green = [(0, d[1], 0) for d in data]
        blue = [(0, 0, d[2]) for d in data]
        red_green = [(d[0], d[1], 0) for d in data]
        red_blue = [(d[0], 0, d[2]) for d in data]
        green_blue = [(0, d[1], d[2]) for d in data]

        img.putdata(red)
        img.save('red.bmp')
        img.putdata(green)
        img.save('green.bmp')
        img.putdata(blue)

    if выбор == '3':
        img = Image.open('red.bmp')
        img = img.convert('L')
        img.save('8.bmp')

        arr = np.asarray(img)
        fltr = np.array([[1 for i in range(arr.shape[1])] for j in range(arr.shape[0])])
        for i in range(1, 8):
            fltr *= 2
            Image.fromarray(fltr & arr).convert('L').save(f'{i}.jpg')

