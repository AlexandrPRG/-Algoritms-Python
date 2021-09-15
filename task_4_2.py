"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
 Результаты анализа сохранить в виде комментариев в файле с кодом.
"""
import itertools
import cProfile

def sieve_eratosfen():
    n = 9900
    sieve = set(range(2, n + 1))
    while sieve:
        prime = min(sieve)
        print(prime, end="\t")
        sieve -= set(range(prime, n + 1, prime))


# sieve_eratosfen()


def without_eratosfen():
    from itertools import count

    i_simple_nomber = 1220
    num = i_simple_nomber
    if i_simple_nomber == 2:
        return f"2-e простое число это {num}"
    elif i_simple_nomber == 1:
        return f"1-e простое число это {num}"
    else:
        simple_i = 2
        for num in (_ for _ in itertools.count(3)):
            for div in (_ for _ in range(3, num+1, 2)):
                    if not num % div:
                        if num == div:
                            simple_i += 1
                            res = div
                        else:
                            break
                        if simple_i == i_simple_nomber:
                            return f"{simple_i}-e простое число это {res}"


print(without_eratosfen())


# def main():
#     sieve_eratosfen()
#     without_eratosfen()


# cProfile.run("main()")

# по результату cProfile алгоритм без решета Эратосфена показывает бОльшую нагруженность