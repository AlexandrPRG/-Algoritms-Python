# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят
# и сколько между ними находится букв.
two_symbols = input("Введите две буквы слитно: ")
first = ord(two_symbols[0].lower())
second = ord(two_symbols[1].lower())
between = abs(first - second) - 1
if between < 0:
    between = 0
if not (first in range(97, 123) and second in range(97, 123) or
    first in range(1072, 1104) and second in range(1072, 1104)):
    print('Введены не буквы или буквы разных алфавитов')
else:
    if first in range(97, 123) and second in range(97, 123):
        print(f'{two_symbols[0]} в алфавите на {first - 96}-м месте\n'
            f'{two_symbols[1]} в алфавите на {second - 96}-м месте\n'
            f'между ними букв: {between}')
    else:
        print(f'{two_symbols[0]} в алфавите на {first - 1071}-м месте\n'
            f'{two_symbols[1]} в алфавите на {second - 1071}-м месте\n'
            f'между ними букв: {between}')
