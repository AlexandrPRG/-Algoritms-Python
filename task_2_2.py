# 2. Посчитать четные и нечетные цифры введенного натурального числа
number = int(input("Введите натуральное число: "))
even_sum, noeven_sum = 0, 0
out = number
while number:
    if number % 10 % 2:
        noeven_sum += 1
    else:
        even_sum += 1
    number = number // 10
print("В числе ", out, "четных цифр:", even_sum, "нечетных цифр", noeven_sum)
