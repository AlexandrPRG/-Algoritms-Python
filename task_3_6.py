"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным
и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint as rv

rand_list = [rv(-100, 100) for _ in range(10)]
print(rand_list)
max_el, ind_max_el = 0, 0
min_el, ind_min_el = rand_list[0], 0
for el in rand_list:
    if el > max_el:
        max_el = el
        ind_max_el = rand_list.index(el)
    if el < min_el:
        min_el = el
        ind_min_el = rand_list.index(el)
if ind_min_el < ind_max_el:
    sum_list = sum(rand_list[ind_min_el+1:ind_max_el])
else:
    sum_list = sum(rand_list[ind_max_el+1:ind_min_el])
print("суммa элементов, находящихся между минимальным и максимальным:", sum_list)
