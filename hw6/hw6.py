from random import randint

print('Это игра угадай число!')
random_num = randint(1, 100)
count = 10

while count != 0:
    user_num = int(input('Введите число в диапазоне от 1 до 100: '))
    if user_num > 100 or user_num < 1:
        print('Введенное вами число не входит в диапазон')
    elif random_num == user_num:
        print(f'Вы угадали загаданное число - {random_num}')
        break
    elif random_num < user_num:
        count -= 1
        print(f'Загаданное число меньше введённого вами, у вас осталось {count} попыток')
    elif random_num > user_num:
        count -= 1
        print(f'Загаданное число больше введённого вами, у вас осталось {count} попыток')

print(f'Вы не угадали, загаданное число - {random_num}')