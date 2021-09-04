# 8. Определить, является ли год, который ввел пользователь, високосным или невисокосным.
year = int(input('Введите год: '))
deny = ''
x1 = year % 100
x2 = year % 100 % 4
x3 = year // 100 % 4

if (not x1 and x2 and not x3) or (not x1 and x2 and x3) or \
        (x1 and x2 and not x3) or (x1 and x2 and x3):
    deny = 'не'
print('Год', deny + 'високосный')
