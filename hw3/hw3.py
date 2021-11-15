from random import randint

li = [randint(1, 10000) for _ in range(999)]

while len(li) > 1:
    li.remove(max(li))
    li.remove(min(li))

print(li[0])

# Получилось сделать максимально короткое решение, хотя я думаю оно не самое быстрое,
# из-за множественного перебора значений