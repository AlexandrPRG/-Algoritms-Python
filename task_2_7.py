"""7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""
from random import randint as rv
checker = rv(5, 1000)
true_n = 0
false_n = 0
for check_num in range(checker+1):
    n = rv(1, 5000000)
    if sum([n for n in range(1, n+1)]) == (n * (n + 1))/2:
        true_n += 1
    else:
        false_n += 1
print(f"Выражение 1+2+...+n = n(n+1)/2 роверено {checker+1} раз. "
      f"Из них верно: {true_n}, неверно: {false_n}")
