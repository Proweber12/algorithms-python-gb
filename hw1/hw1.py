res = {}

for i in range(2, 10):
    count = 0
    for j in range(2, 100):
        if j % i == 0:
            count += 1
            res[i] = count
    print(f' Число {i} делит {count} чисел нацело')

