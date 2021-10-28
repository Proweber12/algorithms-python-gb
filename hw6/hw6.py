from random import sample

numbers = sample(range(-30, 30), 10)

min_num = max_num = numbers[0]
min_idx = max_idx =  0
num_sum = 0

for index, num in enumerate(numbers):
    if num > max_num:
        max_num = num
        max_idx = index
    elif num < min_num:
        min_num = num
        min_idx = index

for j in range(min_idx + 1, max_idx) or range(max_idx + 1, min_idx) :
        num_sum += numbers[j]

print(num_sum)