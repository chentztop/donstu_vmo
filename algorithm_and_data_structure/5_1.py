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

sizes = [100, 500, 1000, 3000, 10000]
num_arrays = 3

average_comparisons = []
average_times = []

for size in sizes:
    total_comparisons = 0
    total_time = 0

    for _ in range(num_arrays):
        arr = [random.randint(0, 9999) for _ in range(size)]
        target = random.randint(0, 9999)

        start_time = time.time()
        result_index, comparisons = linear_search(arr, target)
        end_time = time.time()

        total_comparisons += comparisons
        total_time += end_time - start_time

    average_comparisons.append(total_comparisons / num_arrays)
    average_times.append(total_time / num_arrays)

# Построение диаграммы
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Размер массива')
ax1.set_ylabel('Средние сравнение', color=color)
ax1.plot(sizes, average_comparisons, color=color, marker='o')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Среднее время', color=color)
ax2.plot(sizes, average_times, color=color, marker='x')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Сравнение производительности линейного поиска')
plt.show()
