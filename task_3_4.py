"""4. Определить, какое число в массиве встречается чаще всего.
"""
from random import randint as rv

rand_list = [rv(1, 100) for _ in range(100)]
print(rand_list)
freq = dict()
for el in rand_list:
    if freq.get(el) is None:
        freq.setdefault(el, 1)
    else:
        freq.setdefault(el, freq.pop(el) + 1)
max_vsl = max(freq.values())
if max_vsl != 1:
    for item in freq.items():
        if item[1] == max_vsl:
            print(f"число {item[0]} в массиве встречается чаще всего")
else:
    print("Элементы встречаются по одному разу")
