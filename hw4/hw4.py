from random import randint, triangular

min, max = map(int, input('Введите минимальное число диапазона и максимальное через пробел: ').split())

if min < max:
    print(f'Целое число в введёном промежутке: {randint(min, max)}')
    print(f'Вещественное число в введёном промежутке: {triangular(min, max)}')
else:
    print('Введённое вами минимальное число больше максимального')

start, finish = input('Введите символ с которого будет начинаться диапазон и которым будет заканчиваться через пробел: ').lower().split()

if ord(start) < ord(finish):
    print(f'Буква в введёном промежутке: {chr(randint(ord(start), ord(finish)))}')
else:
    print('Введённый вами начальный символ диапазона больше конечного')