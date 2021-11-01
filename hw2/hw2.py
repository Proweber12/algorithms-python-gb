from random import sample

numbers = sample(range(1000), 5)
num_idx = []

for index, num in enumerate(numbers):
    if num % 2 == 0:
        num_idx.append(index)

print(f'Числа {numbers}, индексы чётных {num_idx}')