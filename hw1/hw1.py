from collections import defaultdict

quantity = int(input('Введите количество предприятий: '))

income_info = defaultdict(list)
amount_profit = 0

for i in range(quantity):
    profit = input('Введите предприятие и его прибыль по квартально(4 суммы) через пробел: ').split()
    income_info['company'].append(profit[0])
    company_profit = 0
    for j in range(1, 5):
        income_info[f'quarter_{j}'].append(profit[j])
        amount_profit += int(profit[j])
        company_profit += int(profit[j])
        average_profit = amount_profit / (4 * quantity)
    income_info[f'general_profit'].append(company_profit)


for n in range(len(dict(income_info)["company"])):
    if dict(income_info)["general_profit"][n] < average_profit:
        print(f'Прибыль компании {dict(income_info)["company"][n]} меньше средней прибыли всех компаний')
    elif dict(income_info)["general_profit"][n] > average_profit:
        print(f'Прибыль компании {dict(income_info)["company"][n]} больше средней прибыли всех компаний')


# Данные для копипаста, чтоб не запариваться

# Газпром 12000 14500 35100 24000
# Сбербанк 31354 32453 95232 32155
# Святой_источник 529 425 315 531
# Тинькоф 31352 43512 10322 42312
# Горячий_ключ 1300 3159 3120 1340