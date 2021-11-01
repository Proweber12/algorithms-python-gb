# Честный вариант
from random import sample

numbers = sample(range(-30, 30), 10)

print(numbers)

smallest_num = numbers[0]
min_num = numbers[1]
count = 0

for i in numbers:
    if i == smallest_num:
        count += 1
    if i < smallest_num:
        smallest_num = i

if count > 1:
    min_num = smallest_num
else:
    for j in numbers:
        if smallest_num < j < min_num:
            min_num = j

print(f'{smallest_num} самое маленькое число, а за ним идёт {min_num}')

# Читерский вариант

numbers.sort()
print(numbers)
print(f'{numbers[0]} самое маленькое число, а за ним идёт {numbers[1]}')