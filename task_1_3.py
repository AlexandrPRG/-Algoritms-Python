# 3. По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
first_point_x, first_point_y = \
    input('Задайте через пробел координаты первой точки: ').split()
second_point_x, second_point_y = \
    input('Задайте через пробел координаты второй точки: ').split()
first_point_x = float(first_point_x)
first_point_y = float(first_point_y)
second_point_x = float(second_point_x)
second_point_y = float(second_point_y)
k = (second_point_x - first_point_x) / (second_point_y - first_point_y)
b = second_point_y - k * first_point_x
plus = '+'
x = 'x'
if b < 0:
    plus = ''
if b == 0 and k == 0:
    k = ''
    plus = ''
    x = ''
elif b == 0 and k == 1:
    b = ''
    plus = ''
    k = ''
elif k == 0:
    x = ''
    k = ''
    plus = ''
elif k == 1:
    k = ''
elif k == -1:
    k = '-'
else:
    k = round(k, 1)
    b = round(b, 1)
print('Уравнение прямой:\ny={}{}{}{}'.format(k, x, plus, b))
