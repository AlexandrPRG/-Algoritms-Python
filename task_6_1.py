"""1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
 в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
 эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной
 и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях
  версию Python и разрядность вашей ОС.
"""
from sys import getsizeof as sg, getrefcount as sgc
import collections
import task_3_3, task_3_4, task_3_5

vars = [[var
        for var in dir(modul) if var[0] != '_']
        for modul in [task_3_3, task_3_4, task_3_5]]
total_vars = [[var
        for var in dir(modul)]
        for modul in [task_3_3, task_3_4, task_3_5]]
# type_vars = [[var.__class__
#         for var in dir(modul)]
#         for modul in [task_3_3, task_3_4, task_3_5]]
types = []
type_vars = []
m = sg(task_3_3.el) + sg(task_3_3.el.__class__)
types.append(m)
m = sg(task_3_3.rv) + sg(task_3_3.rv.__class__)
types.append(m)
m = sg(task_3_3.min_el) + sg(task_3_3.min_el.__class__)
types.append(m)
m = sg(task_3_3.max_el) + sg(task_3_3.max_el.__class__)
types.append(m)
m = sg(task_3_3.rand_list) + sg(task_3_3.rand_list.__class__)
types.append(m)
m = sg(task_3_3.ind_min_el) + sg(task_3_3.ind_min_el.__class__)
types.append(m)
m = sg(task_3_3.ind_max_el) + sg(task_3_3.ind_max_el.__class__)
types.append(m)
type_vars.append(types.copy())
types.clear()

m = sg(task_3_4.el) + sg(task_3_4.el.__class__)
types.append(m)
m = sg(task_3_4.rv) + sg(task_3_4.rv.__class__)
types.append(m)
m = sg(task_3_4.rand_list) + sg(task_3_4.rand_list.__class__)
types.append(m)
m = sg(task_3_4.freq) + sg(task_3_4.freq.__class__)
types.append(m)
m = sg(task_3_4.max_vsl) + sg(task_3_4.max_vsl.__class__)
types.append(m)
m = sg(task_3_4.item) + sg(task_3_4.item.__class__)
types.append(m)
type_vars.append(types.copy())
types.clear()

m = sg(task_3_5.el) + sg(task_3_5.el.__class__)
types.append(m)
m = sg(task_3_5.rv) + sg(task_3_5.rv.__class__)
types.append(m)
m = sg(task_3_5.max_el) + sg(task_3_5.max_el.__class__)
types.append(m)
m = sg(task_3_5.rand_list) + sg(task_3_5.rand_list.__class__)
types.append(m)
m = sg(task_3_5.sign) + sg(task_3_5.sign.__class__)
types.append(m)
m = sg(task_3_5.ind_max) + sg(task_3_5.ind_max.__class__)
types.append(m)
type_vars.append(types.copy())
types.clear()

for list_var in vars:
    name_module = [task_3_3, task_3_4, task_3_5][vars.index(list_var)].__name__
    for var in list_var:
        print("Переменная", var, "модуля", name_module, "занимает", sg(var), "бит")
print(total_vars)
print(len(total_vars))
for modul in type_vars:
    name_module = [task_3_3, task_3_4, task_3_5][type_vars.index(modul)].__name__
    print("Переменные модуля", name_module, "используют", sum(modul), "бит")
