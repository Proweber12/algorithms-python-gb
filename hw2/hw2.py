num = input('Введите число: ')

even = 0
odd = 0

for digit in num:
    if int(digit) % 2 == 0:
        even += 1
    elif int(digit) % 2 != 0:
        odd += 1

print(f'В числе {num} четных - {even}, нечетных - {odd}')