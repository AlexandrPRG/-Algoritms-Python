# 9. Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).
numbers = [int(input('Введите ' + str(ind + 1) + '-е число: '))
           for ind in range(3)]
print('Среднее ', str(numbers.index(sorted(numbers)[1])+1) + "-е число",
      sorted(numbers)[1])