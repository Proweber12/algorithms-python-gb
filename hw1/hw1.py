print('Вы вошли в калькулятор')

while True:
    user_input = input('Введите число, потом арефметический знак(+, -, *, /), затем второе число,\nа если хотите завершить работу в калькуляторе просто введите 0: ').split()
    match user_input:
        case a, '+', b if str.isdigit(a) and str.isdigit(b):
            print(f'\nРешение: {a} + {b} = {int(a) + int(b)}\n')
        case a, '-', b if str.isdigit(a) and str.isdigit(b):
            print(f'\nРешение: {a} - {b} = {int(a) - int(b)}\n')
        case a, '*', b if str.isdigit(a) and str.isdigit(b):
            print(f'\nРешение: {a} * {b} = {int(a) * int(b)}\n')
        case a, '/', b if int(b) > 0 and str.isdigit(a) and str.isdigit(b):
            print(f'\nРешение: {a} / {b} = {round(int(a) / int(b), 3)}\n')
        case '0',:
            print('\nКалькулятор выключен')
            break
        case _:
            print('\nВведены неверные данные\n')
