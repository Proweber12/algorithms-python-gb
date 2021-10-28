from random import randint

numbers = [randint(0, 10) for _ in range(20)]

print(numbers)

count = 0
number = 0

for i in numbers:
    if numbers.count(i) > count:
        count = numbers.count(i)
        number = i

print(f'Число {number}, встречается чаще всего({count} раз(-а))')