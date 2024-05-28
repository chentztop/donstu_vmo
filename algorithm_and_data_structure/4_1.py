import random
import time


# Функция для сортировки пузырьком
def bubble_sort(arr):
    n = len(arr)
    iterations = 0
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            iterations += 1
            comparisons += 1
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return iterations, comparisons, swaps


# Функция для сортировки выбором
def selection_sort(arr):
    n = len(arr)
    iterations = 0
    comparisons = 0
    swaps = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            iterations += 1
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        swaps += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return iterations, comparisons, swaps


# Функция для сортировки вставками
def insertion_sort(arr):
    n = len(arr)
    iterations = 0
    comparisons = 0
    swaps = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        iterations += 1

        while j >= 0 and key < arr[j]:
            comparisons += 1
            swaps += 1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return iterations, comparisons, swaps


# Генерация массива случайных чисел
def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]


# Ввод массива с клавиатуры
def input_array():
    size = int(input("Введите размер массива: "))
    return [int(input(f"Введите элемент {i + 1}: ")) for i in range(size)]


# Тестирование сортировок на различных размерах массивов
sizes = [20, 500, 1000, 3000, 5000, 10000]

for size in sizes:
    if size == 20:
        arr = input_array()
    else:
        arr = generate_random_array(size)

    print(f"\nСортировка массива размером {size} элементов:")

    start_time = time.time()
    _, comp_bubble, swap_bubble = bubble_sort(arr.copy())
    bubble_time = time.time() - start_time

    start_time = time.time()
    _, comp_selection, swap_selection = selection_sort(arr.copy())
    selection_time = time.time() - start_time

    start_time = time.time()
    _, comp_insertion, swap_insertion = insertion_sort(arr.copy())
    insertion_time = time.time() - start_time

    print("Сортировка пузырьком:")
    print(f"Итераций: {_}, Сравнений: {comp_bubble}, Обменов: {swap_bubble}, Время: {bubble_time:.6f} сек")

    print("Сортировка выбором:")
    print(f"Итераций: {_}, Сравнений: {comp_selection}, Обменов: {swap_selection}, Время: {selection_time:.6f} сек")

    print("Сортировка вставками:")
    print(f"Итераций: {_}, Сравнений: {comp_insertion}, Обменов: {swap_insertion}, Время: {insertion_time:.6f} сек")
