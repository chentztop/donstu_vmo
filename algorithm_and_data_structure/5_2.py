import numpy as np
import matplotlib.pyplot as plt
import time
import random

def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    comparisons = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons

sizes = [100, 500, 1000, 3000, 10000]
num_arrays = 3

average_comparisons_linear = []
average_times_linear = []
average_comparisons_binary = []
average_times_binary = []

for size in sizes:
    total_comparisons_linear = 0
    total_time_linear = 0
    total_comparisons_binary = 0
    total_time_binary = 0

    for _ in range(num_arrays):
        arr = sorted([random.randint(0, 9999) for _ in range(size)])
        target = random.randint(0, 9999)

        start_time = time.time()
        result_index, comparisons = linear_search(arr, target)
        end_time = time.time()

        total_comparisons_linear += comparisons
        total_time_linear += end_time - start_time

        start_time = time.time()
        result_index, comparisons = binary_search(arr, target)
        end_time = time.time()

        total_comparisons_binary += comparisons
        total_time_binary += end_time - start_time

    average_comparisons_linear.append(total_comparisons_linear / num_arrays)
    average_times_linear.append(total_time_linear / num_arrays)
    average_comparisons_binary.append(total_comparisons_binary / num_arrays)
    average_times_binary.append(total_time_binary / num_arrays)

# Построение диаграммы
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Размер массива')
ax1.set_ylabel('Среднее сравнение', color=color)
ax1.plot(sizes, average_comparisons_linear, color=color, marker='o', label='Линейный поиск')
ax1.plot(sizes, average_comparisons_binary, color='tab:blue', marker='x', label='Бинарный поиск')
ax1.tick_params(axis='y', labelcolor=color)
plt.legend(loc='upper left')

ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Время выполнения', color=color)
ax2.plot(sizes, average_times_linear, color=color, marker='o', label='Линейный поиск')
ax2.plot(sizes, average_times_binary, color='tab:purple', marker='x', label='Бинарный поиск')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Линейниый поиск vs Бинарный поиск')
plt.show()
