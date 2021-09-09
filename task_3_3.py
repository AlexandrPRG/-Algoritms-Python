"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный
 элементы.
"""
from random import randint as rv

rand_list = [rv(1, 100) for _ in range(10)]
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
rand_list.insert(ind_min_el, max_el)
rand_list.pop(ind_min_el+1)
rand_list.insert(ind_max_el, min_el)
rand_list.pop(ind_max_el+1)
print(rand_list)
