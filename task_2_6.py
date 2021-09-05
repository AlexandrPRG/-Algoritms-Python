"""6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное
 пользователем число, чем то, что загадано.
 Если за 10 попыток число не отгадано, то вывести загаданное число.
"""
from random import randint as rn


def enter_val():
    while True:
        try:
            return int(input("Отгадайте загаданное число (от 0 до 100): "))
        except ValueError:
            print("Это не целое число!")


number = rn(0, 100)
for attempt in range(1, 11):
    custom_val = enter_val()
    if custom_val == number:
        print(f"Вы угадали с {attempt}-й попытки!")
        exit(0)
    elif custom_val < number:
        print(f"Попытка {attempt}. Загаданное число больше")
    else:
        print(f"Попытка {attempt}. Загаданное число меньше")
print(f"Загаданное число {number}.")
