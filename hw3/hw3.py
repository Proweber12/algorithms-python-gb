from random import sample

numbers = sample(range(1000), 5)
print(numbers)

min_num = numbers[0]
max_num = numbers[0]

min_idx = 0
max_idx = 0

for index, num in enumerate(numbers):
    if num > max_num:
        max_num = num
        max_idx = index
    elif num < min_num:
        min_num = num
        min_idx = index

numbers[max_idx], numbers[min_idx] = numbers[min_idx], numbers[max_idx]

print(numbers)