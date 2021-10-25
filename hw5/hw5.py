for i in range(32, 128):
    if (i - 32) % 10 != 0 or i == 32:
        print(f'{ord(chr(i))} - {chr(i)}         ', end='')
    else:
        print('\n')
        print(f'{ord(chr(i))} - {chr(i)}         ', end='')
