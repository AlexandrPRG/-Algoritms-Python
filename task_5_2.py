"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
число представляется как массив, элементы которого это цифры числа.
 Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
 Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
first_val = list(input("Первое шестнадцатиричное число: "))
second_val = list(input("Второе шестнадцатиричное число: "))
first_val = int(''.join(first_val), 16)
second_val = int(''.join(second_val), 16)
print("Сумма", list(str(hex(first_val + second_val)).upper())[2:])
print("произведение", list(str(hex(first_val * second_val)).upper())[2:])
