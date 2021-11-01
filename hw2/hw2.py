import cProfile
import math

# С "Решетом Эратосфена"

# Выполнение с диапазоном простых чисел до 1000 и нахождением 100-ого простого числа - 0.001 секунды
# Выполнение с диапазоном простых чисел до 10000 и нахождением 1000-ого простого числа - 0.049 секунды
# Выполнение с диапазоном простых чисел до 100000 и нахождением 9000-ого простого числа - 7.111 секунд

def eratosphene(n, count_num):

    sieve = set(range(2, n+1))
    count = 0

    while sieve:
        prime = min(sieve)
        sieve -= set(range(prime, n+1, prime))
        count += 1
        if count == count_num:
            print(f'{prime} - это {count}-ое простое число по счёту')
            break

    if count < count_num:
        print(f'В данном диапазоне нет {count_num}-ого простого числа по счёту')


cProfile.run('eratosphene(1000, 100)')

# Без "Решета Эратосфена"

# Выполнение с диапазоном простых чисел до 1000 и нахождением 100-ого простого числа - 0.015 секунды
# Выполнение с диапазоном простых чисел до 10000 и нахождением 1000-ого простого числа - 0.126 секунды
# Выполнение с диапазоном простых чисел до 100000 и нахождением 9000-ого простого числа - 2.007 секунды

def not_eratosphene(n, count_num):

    def is_prime(i):
        m = min(i, int(math.sqrt(n)))
        l = range(2, m)
        r = map(lambda x: i % x == 0, l)
        return not any(r)

    sieve = list(filter(is_prime, range(2, n+1)))

    for i, v in enumerate(sieve):
        if count_num == i+1:
            print(f'{v} - это {i+1}-ое простое число по счёту')
            break

cProfile.run('not_eratosphene(100000, 9000)')

# На мой взгляд второй алгоритм более сложный в написании для него я использовал большее количество всяких функций
# и логических операций
# Скорость выполнения программ оказалась интересной, так как я ожидал, что если первых два теста с меньшими числами выполнятся
# в варианте с решетом быстрей, то и третий должен быть также быстрей, но оказалось так, что версия без решета работает
# с большими числами быстрей, а с маленькими меделеней