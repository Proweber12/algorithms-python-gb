# Пришлось считерить, чтобы догнать программу, но я как-нибудь попробую перерешать эту задачу "вручную"

num_1 = list(input('Введите первое шестнадцатерицное число: ').lower())
num_2 = list(input('Введите второе шестнадцатерицное число: ').lower())

amount = list(hex(int(''.join(num_1), base = 16) + int(''.join(num_2), base = 16)).upper())
mult = list(hex(int(''.join(num_1), base = 16) * int(''.join(num_2), base = 16)).upper())
print(f'Сумма: {amount[2:]}')
print(f'Произведение: {mult[2:]}')

