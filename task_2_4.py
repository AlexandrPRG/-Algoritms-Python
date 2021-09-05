"""4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
list_seqence = []
sum_val = 0
m = 1
n = int(input("Введите количество элементов: "))
while n:
    list_seqence.append(m)
    sum_val = sum_val + m
    m = m / -2
    n -= 1
print("Сумма последовательности {", *list_seqence, "} =\n", sum_val)
