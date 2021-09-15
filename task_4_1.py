"""1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
# анализ алгоритма task_2_1
import cProfile
import timeit


def variant_1():
    str_out = {}
    interval_natural = (n for n in range(2, 100))
    for natural in interval_natural:
        interval_decimal = (n for n in range(2, 10))
        for dec in interval_decimal:
            if not natural % dec:
                if str_out.get(dec) is not None:
                    str_out.setdefault(dec, str_out.pop(dec) + 1)
                else:
                    str_out.setdefault(dec, 1)
    print("Вариант 1\n")
    for key in str_out.keys():
        print(f"{key}-и(м) кратно {str_out[key]} чисел из дапазона 2-99")


def variant_2():
    str_out = []
    counter = 0
    natural = [n for n in range(2, 100)]
    decimal = [n for n in range(2, 10)]
    for decim in decimal:
        for natur in natural:
            if not natur % decim:
                counter += 1
        str_out.append(counter)
        counter = 0
    print("Вариант 2\n")
    for id, el in enumerate(str_out):
        print(f"{id + 2}-и(м) кратно {el} чисел из дапазона 2-99")


def variant_3():
    str_out = [sum(1 if not natur % decim else 0
                for natur in [n for n in range(2, 100)]
                for decim in [n]) for n in range(2, 10)]
    print("Вариант 3\n")
    for id, el in enumerate(str_out):
        print(f"{id + 2}-и(м) кратно {el} чисел из дапазона 2-99")


def main():
    variant_1()
    variant_2()
    variant_3()


print(timeit.default_timer())
cProfile.run('main()')

"""
результаты профилирования показывают, что самым нагрузочным алгоритмом является 
variant_1, так как в нем используется словарь, который и оттягивает много ресурсов.
"""