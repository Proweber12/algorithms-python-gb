from random import sample

numbers = sample(range(-30, 30), 10)

print(numbers)

max_negative_num = min(numbers)
idx = 0

for index, num in enumerate(numbers):
    if num < 0 and num > max_negative_num:
        max_negative_num = num
        idx = 0

print(f'Максимальное отрицательное число {max_negative_num}, его индекс {idx}')

