import random
import time

# Функция бинарного поиска
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iteration_count = 0
    while low <= high:
        iteration_count += 1
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid, iteration_count
    return -1, iteration_count

# Генерация случайного массива
size = 1000 # Размер массива
arr = [random.randint(1, 10000) for _ in range(size)]
arr.sort() # Сортировка массива

# Элемент для поиска
x = random.choice(arr)

# Измерение времени и количества итераций
start_time = time.time()
index, iterations = binary_search(arr, x)
end_time = time.time()

# Вывод результатов
if index != -1:
    print(f"Элемент найден на позиции: {index}")
else:
    print("Элемент не найден в массиве")
print(f"Количество итераций: {iterations}")





