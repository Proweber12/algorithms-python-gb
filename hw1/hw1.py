import hashlib

line = input('Введите строку маленькими латинскими буквами: ')

hash_word = set()

if line.islower() and line.isalpha():
    for i in range(len(line)):
        for j in range(len(line), i, -1):
            hash_word.add(hashlib.sha1(line[i:j-1].encode('utf-8')).hexdigest())
    print(f'{len(hash_word)} различных подстрок в строке {line} \n↓ВСЕ ХЭШИ ПОДСТРОК↓ \n{hash_word}')
else:
    print("Введенная строка не соответствует правилам")
