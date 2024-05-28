import time
import random




def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


sizes = [20, 500, 1000, 3000, 5000, 10000]

print("Size\tQuick Sort Time")
for size in sizes:
    arr = [random.randint(0, size) for _ in range(size)]

    start_time = time.time()
    quick_sorted = quick_sort(arr.copy())
    quick_time = time.time() - start_time

    print(f"{size}\t{quick_time:.6f}")
