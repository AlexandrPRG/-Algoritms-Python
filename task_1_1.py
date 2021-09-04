# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
m_nomber = int(input('Введите трехзначное число >> '))
sumr = 0
multr = 1
for ind in range(3):
    r = m_nomber % 10
    m_nomber = m_nomber // 10
    sumr = sumr + r
    multr = multr * r
print('Сумма цифр: ', sumr, '\n'
      'Произведение цифр: ', multr)
