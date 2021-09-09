"""8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""


def check_matrix(val):
    while True:
        try:
            return int(val)
        except ValueError:
            print("Это не число: ")


m = 3
n = 5
res_matrix = []
matrix = [[check_matrix(input(f"Элемент ({row},{clmn}): ")) for clmn in range(1, m+1)]
          for row in range(1, n+1)]
# matrix = [[11,12,13],[21,22,23],[31,32,33],[41,42,43],[51,52,53]]
print('Матрица:\n' + '\n'.join('\t'.join(map(str, el_row))
                                    for el_row in matrix))
for row in matrix:
    row.append(sum(row))
    res_matrix.append(row)
print('Результат:\n' + '\n'.join('\t'.join(map(str, el_row))
                                    for el_row in res_matrix))
