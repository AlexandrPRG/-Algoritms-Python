# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

# «И», «ИЛИ» и др. над числами 5 и 6
print(5^6)
print(5&6)
print(not 5)
print(not 6)
# 5 побитовый сдвиг вправо и влево
print(5>>2)
print(5<<2)

print(bin(5), bin(6))
# число 5 в двоичной системе счисления равно 101.
# число 6 в двоичной системе счисления равно 110.
# "исключительное или" 101^110 равно 011, что в десятичной системе 3.
# "и" 101&110 равно 100, что в десятичной системе 4.
# сдвиг вправо 101 по битам первый: 10, второй: 1, что в десятичной системе 1.
# сдвиг влево 101 по битам первый: 1010, второй: 10100, что в десятичной системе 20.
