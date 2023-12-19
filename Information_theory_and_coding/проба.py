
import struct

file = 'image.bmp'

with open(file, 'rb') as f:
    # читаем первые 14 байт - заголовок файла
    header = f.read(54)

    # распаковываем заголовок
    b1, b2, b3, b4, b5, b6, b7,b8, b9, b10, b11, b12, b13, b14, b15, b16 = struct.unpack('<2sIHHIIIIHHIIIIII', header)

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

from PIL import Image
import numpy as np

img = Image.open('image.bmp')
data = np.array(img.getdata())

red = [(d[0], 0, 0) for d in data]
green = [(0, d[1], 0) for d in data]
blue = [(0, 0, d[2]) for d in data]
red_green = [(d[0], d[1],0) for d in data]
red_blue = [(d[0], 0, d[2]) for d in data]
green_blue = [(0, d[1], d[2]) for d in data]

img.putdata(red)
img.save('red.bmp')
img.putdata(green)
img.save('green.bmp')
img.putdata(blue)
img.save('blue.bmp')
img.putdata(red_green)
img.save('red_green.bmp')
img.putdata(red_blue)
img.save('red_blue.bmp')
img.putdata(green_blue)
img.save('green_blue.bmp')

img = Image.open('image.bmp')
img = img.convert('L')
img.save('8.bmp')

arr = np.asarray(img)
fltr = np.array([[1 for i in range (arr.shape[1])]for j in range (arr.shape[0])])
for i in range(1,8):
    fltr *= 2
    Image.fromarray(fltr&arr).convert('L').save(f'{i}.jpg')
