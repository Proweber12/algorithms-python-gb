import time
from random import uniform, seed

# Время выполнения: 0.028632499999999998

start = time.perf_counter()

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            arr[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            arr[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        arr[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        arr[left_cursor + right_cursor] = right[right_cursor]

    return arr

seed(42)
li = [uniform(0, 49) for _ in range(1000)]
print(f'Исходный массив: {li}')
merge_sort(li)
print(f'Отсортированый массив: {li}')

print(f'Время выполнения: {time.perf_counter() - start}')