numbers = input('Введите натуральные числа: ').split()

max = 0
digit = 0

for num in numbers:
    sum = 0
    for i in num:
        sum += int(i)
    if sum > max:
        max = sum
        digit = num

print(f'Максимальное число последовательности - {digit}, сумма его цифр равна - {max}')
