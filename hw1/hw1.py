# ОС - Windows 10(x64)
# Python 3.10

from pympler import asizeof
from random import randint
from collections import Counter
from sys import getsizeof

# В ходе анализа заметил неявное различие модуля pympler с функцией asizeof(рекурсивное оценивание)
# и модуля sys с функцией getsizeof(поверхностное оценивание) по отношению к числам(со списками и т.д. итак всё понятно).
# Выявил, что x = 0 в обеих случаях это значение равно 24 байтам,
# но когда делаю x = 1, pympler показвает 32 байта, а sys 28 байт.
# Предположительно эта разница из-за каких-то особенностей хранения объекта типа integer в Python
# Такое же различие в 4 байта было замечено при замерении размера, которое занимает самое популярное число
# с помощью модуля collections
# При сравнении показателей оценивания размера памяти, которую занимает введёный текст в зависимости от длинны строки
# pympler с функцией asizeof на 1-6 байта больше, чем sys с функцией getsizeof

# Программа находящая число встречающееся чаще всего(2 варианта)

# Вариант 1

numbers = [randint(1, 1000) for _ in range(1001)]

count = 0
number = 1
print(f'{asizeof.asizeof(count)}bytes занимает переменная со значением 0 в рекурсивном оценивании')
print(f'{getsizeof(count)}bytes занимает переменная со значением 0 в поверхностном оценивании \n')
print(f'{asizeof.asizeof(number)}bytes занимает переменная со значением 1 в рекурсивном оценивании')
print(f'{getsizeof(number)}bytes занимает переменная со значением 1 в поверхностном оценивании \n')

for i in numbers:
    if numbers.count(i) > count:
        count = numbers.count(i)
        number = i

print(f'{asizeof.asizeof(numbers)}bytes занимает список из 1000 элементов \n')

# Вариант 2

popular_number = Counter(numbers).most_common(1)

print(f'{asizeof.asizeof(popular_number[0][0])}bytes занимает переменная сортировки в рекурсивном оценивании')
print(f'{getsizeof(popular_number[0][0])}bytes занимает переменная сортировки в поверхностном оценивании \n')

# Программа реверса числа

num = input('Введите число: ')

for i in num[::-1]:
    print(i, end='')

print(f'\n{asizeof.asizeof(num)}bytes занимает переменная ввода текста в рекурсивном оценивании')
print(f'{getsizeof(num)}bytes занимает переменная ввода текста в поверхностном оценивании')