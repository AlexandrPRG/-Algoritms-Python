"""3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
"""
from random import randint as rv

if __name__ == '__main__':
    m = 2
    massive = [rv(-100, 100) for _ in range(2 * m + 1)]
    less_counter, more_counter, equal_counter = 0, 0, 0
    for mediana in massive:
        for el in massive:
            if not (less_counter > len(massive) / 2 + 1
                    or more_counter > len(massive) / 2 + 1):
                if el < mediana:
                    less_counter += 1
                elif el > mediana:
                    more_counter += 1
                else:
                    equal_counter -= 1
        if abs(less_counter - more_counter) + equal_counter < 0:
            print(massive)
            print("Медиана:", mediana)
            exit(0)
        less_counter, more_counter, equal_counter = 0, 0, 0
