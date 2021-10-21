year = int(input('Введите год: '))

if year < 1582:
    print('До 1582 года високосных лет не существовало')
elif year % 400 == 0:
    print(f'{year} - високосный год')
elif year % 4 == 0 and year % 100 != 0:
    print(f'{year} - високосный год')
else:
    print(f'{year} - невисокосный год')