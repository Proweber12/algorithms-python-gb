# Определить, какое число в массиве встречается чаще всего

# Вариант 1

from random import randint
from collections import Counter
import cProfile

numbers = [randint(0, 10) for _ in range(1000)]



def number_popular():

    count = 0
    number = 0

    for i in numbers:
        if numbers.count(i) > count:
            count = numbers.count(i)
            number = i

    print(f'Число {number}, встречается чаще всего({count} раз(-а))')

cProfile.run('number_popular()')

# Вариант 2

def number_popular_2():

    print(Counter(numbers).most_common(1))

cProfile.run('number_popular_2()')
