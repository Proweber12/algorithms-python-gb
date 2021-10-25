n = int(input('Введите количество элементов ряда: '))

sum = 0
div = -2
digit = 1

for i in range(n):
    sum += digit
    digit /= div

print(f'Сумма: {sum}')