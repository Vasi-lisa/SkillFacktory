money = int(input('Сумма вклада:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for key in per_cent:
    deposit.append(int(money * per_cent[key]/100))

deposit_i = max(deposit)
print('Сумма, которую можно заработать в каждом банке', deposit)
print('Максимальная сумма, которую вы можете заработать:', deposit_i)