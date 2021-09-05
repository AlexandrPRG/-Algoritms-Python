"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
 Числа и знак операции вводятся пользователем. После выполнения вычисления программа не
должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы
должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
 неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
 и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления
 на ноль, если он ввел 0 в качестве делителя.
"""
def check_operand(val):
        try:
            return float(val)
        except ValueError:
            print("Нужно число: ")
            return None


def check_operator(val):
    operation_list = ('0', '+', '-', '*', '/')
    if val in operation_list:
        return val
    else:
        print("Операция не поддерживается")
        return None


operand_1, operator, operand_2, checker = None, None, None, False
while not checker:
    print("Вычисления с двумя числами")
    while operand_1 is None:
        operand_1 = check_operand(input('Введите первый операнд: '))
    while not operator:
        operator = check_operator(input('Введите операцию +-*/(0-выход): '))
    while operand_2 is None:
        operand_2 = check_operand(input('Введите второй операнд: '))
    str_out = f"{operand_1} {operator} {operand_2} ="
    checker = operator
    if operator == '/':
        if operand_2:
            str_out = f"{str_out} {round(operand_1 / operand_2, 2)}"
        else:
            str_out = f"На ноль не делю, к сожалению"
    elif operator == '*':
        str_out = f"{str_out} {round(operand_1 * operand_2, 2)}"
    elif operator == '-':
        str_out = f"{str_out} {round(operand_1 - operand_2, 2)}"
    elif operator == '+':
        str_out = f"{str_out} {round(operand_1 + operand_2, 2)}"
    else:
        checker = True
        str_out = 'Выход'
    operand_1, operator, operand_2 = None, None, None
    print(str_out)
