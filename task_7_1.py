"""1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный
случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его
умнее)."""
from random import randint as rv
import timeit

rand_list = [rv(-100, 100) for _ in range(10000)]


def sort_rand_list(lst: list):
    cutter = 1
    checker = len(lst[:-cutter])
    # print(lst)
    while checker:
        for ind, el in enumerate(lst[:-cutter]):
            if el < lst[ind+1]:
                lst[ind], lst[ind+1] = lst[ind+1], el
                cutter = 1
                break
            cutter += 1
            checker = len(lst[:-cutter])
    return lst


def calmer_sort(lst: list):
    cutter = 1
    checker = True
    # print(lst)
    while checker:
        for ind, el in enumerate(lst[:-cutter]):
            if el != lst[ind+1]:
                if el < lst[ind+1]:
                    lst[ind], lst[ind+1] = lst[ind+1], el
                    cutter = 1
                    checker = True
                    break
                else:
                    checker = False
                cutter += 1
    return lst


if __name__ == '__main__':
    print(timeit.timeit('sort_rand_list(rand_list)', number=10, globals=globals()))
    print(timeit.timeit('calmer_sort(rand_list)', number=10, globals=globals()))


"""
rand_list  sort_rand_list  calmer_sort            calmer_sort < sort_rand_list
10         0.0242811       0.015339000000000005   63,17%
100        0.3555214       0.09690480000000001    27,25%
1000       172.5841435     9.0044497              94,78%
Средний выигрыш производительности 61,73%      
"""
