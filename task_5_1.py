"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить
среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
"""
import collections

name_company = collections.defaultdict(int)
quantity = 3
for _ in range(quantity):
    name = input("Предприятие: ")
    sum_profit = int(sum([int(input("Прибыль " + str(prof) + "-го квартала: "))
                          for prof in range(1, 5)]))
    name_company[name] = sum_profit

average_profit = sum(prof for prof in name_company.values()) / quantity
supra_profit = [name for name, prof in name_company.items() if prof > average_profit]
infra_profit = [name for name, prof in name_company.items() if prof < average_profit]
print("средняя прибыль за год для всех предприятий:", round(average_profit))
print("список предприятий, чья прибыль ниже среднего:", infra_profit)
print("список предприятий, чья прибыль выше среднего:", supra_profit)
