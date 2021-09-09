"""2. Во втором массиве сохранить индексы четных элементов первого массива. .
"""
from random import randint as rv

first_list = list(set(rv(1, 100) for _ in range(50)))
sec_list = [first_list.index(n) for n in first_list if not n % 2]
print(first_list)
print(sec_list)