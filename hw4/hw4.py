from random import randint

numbers = [randint(0, 10) for _ in range(20)]
print(numbers)

for i in numbers:
    print(numbers.count(i), end=', ')