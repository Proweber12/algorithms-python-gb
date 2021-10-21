a, b, c = map(int, input('Введите длину отрезков треугольника через пробел: ').split())

if a + b <= c and a + c <= b and b + c <= a:
    print('Такой треугольник не существует')
else:
    if a == b and b == c:
        print('Треугольник равносторонний')
    elif (a == b and b != c) or (c == b and a != c) or (a == c and c != b):
        print('Треугольник равнобедренный')
    elif a != b and b != c and c != a:
        print('Треугольник разносторонний')
