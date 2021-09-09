"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве
"""
from random import randint as rv

rand_list = [rv(-100, 100) for _ in range(100)]
max_el = 0
ind_max = 0
sign = False
for el in rand_list:
    if el < 0:
        if sign:
            if abs(max_el) > abs(el):
                max_el = el
                ind_max = rand_list.index(el)
        else:
            sign = True
            max_el = el
            ind_max = rand_list.index(el)
if max_el:
    print(max_el, "- максимальный отрицательный элемент на позиции ", ind_max)
else:
    print("отрицательный элемент в массиве не найден")
