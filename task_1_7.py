# 7. По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он
# разносторонним, равнобедренным или равносторонним.
cutters = [float(input('длина ' + str(ind + 1) + '-й стороны треугольника: '))
           for ind in range(3)]
perimeter = sum(cutters)
form_tr = len(set(cutters))
str_out = 'треугольник существует и является '
for cutter in cutters:
    if cutter >= perimeter - cutter:
        print('треугольник не существует')
        exit()
if form_tr == 3:
    str_out = str_out + 'разносторонним'
elif form_tr == 2:
    str_out = str_out + 'равнобедренным'
else:
    str_out = str_out + 'равносторонним'
print(str_out)
