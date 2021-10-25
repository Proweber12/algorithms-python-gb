*numbers, digit = input('Введите последовательность чисел и цифру, которую необходимо посчитать - ').split()

count = 0

for num in numbers:
    for i in num:
        if digit == i:
            count += 1

print(f'Цифра {digit} встретилась {count} раз(-а)')