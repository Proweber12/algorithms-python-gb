n = int(input('Введите натуральное число: '))

sum = 0

for i in range(1, n+1):
    sum += i

formula = n * (n + 1) / 2

print(f' 1+2+...+n = {sum} \n n * (n + 1) / 2 = {int(formula)}')
print('Значит 1+2+...+n = n * (n + 1) / 2')