"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
 Вывести на экран это число и сумму его цифр
"""
from random import randint as rv
inp_list = [rv(1, n) for n in range(1, rv(1, 1000000))]
max_sum_digit = 0
for el in inp_list:
    sum_digit = 0
    prev_el = el
    while el:
        sum_digit = sum_digit + int(el % 10)
        el = el // 10
    if sum_digit >= max_sum_digit:
        max_sum_digit = sum_digit
        max_el = prev_el
print(f"Среди {len(inp_list)} чисел наибольшее по сумме цифр {max_el}. Сумма его цифр {max_sum_digit}")
