letter_number = int(input('Введите порядковый номер латинской буквы в алфавите: '))

if letter_number > 0 and letter_number < 27:
    print(f'Вы ввели порядковый номер буквы - {chr(letter_number + 96)}')
else:
    print('Вы ввели число не соответствующее порядковому номеру буквы латинского алфавита')