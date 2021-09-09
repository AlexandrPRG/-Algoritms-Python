"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
from random import randint as rv

rand_list = [rv(-100, 100) for _ in range(10)]
print(rand_list)
n = 2   # число необходимых минимальных элементов
min_list = []
ind_min_list = []
for _ in range(n):
    if len(ind_min_list) == 1 and ind_min_list[0] == 0:
        min_el = rand_list[1]
    else:
        min_el = rand_list[0]
    ind_min_el = rand_list.index(min_el)
    for el_index, el in enumerate(rand_list):
        if el_index not in ind_min_list:
            if  el not in min_list:
                if el < min_el:
                    min_el = el
                    ind_min_el = el_index
            else:
                ind_min_list.append(el_index)
                min_list.append(el)
    min_list.append(min_el)
    ind_min_list.append(ind_min_el)
print(n, " наименьших элемента:", *min_list[:n])
print("на позициях: ", *ind_min_list[:n])
