"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр
 и вывести на экран
"""
number = int(input("Введите натуральное число: "))
str_out = ''
while number:
    str_out = str_out + str(number % 10)
    number = number // 10
print(str_out)
