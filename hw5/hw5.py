start, finish = input('Введите латинский символ с которого будет начинаться диапазон и которым будет заканчиваться через пробел: ').lower().split()

if ord(start) < ord(finish):
    print(f'Вы ввели букву {start} - это {ord(start)-96}-ая буква алфавита')
    print(f'Также вы ввели букву {finish} - это {ord(finish)-96}-ая буква алфавита')
    print(f'Промежуток между этими буквами равен {(ord(finish)-96) - (ord(start)-96) - 1} символов')
else:
    print('Введённый вами начальный символ диапазона больше конечного')