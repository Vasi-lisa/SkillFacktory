bilet = int(input('Количество билетов, которые вы желаете преобрести:'))
price = 0

for i in range(bilet):
    age = int(input('Введите возраст посетителя:'))
    if age < 18:
        price += 0
        print('Бесплатно')
    elif 18 < age < 25:
        price += 990
        print('990 рублей')
    elif age > 25:
        price += 1390
        print('1390 рублей')
if bilet > 3:
    discount = price * 0.1

print('Сумма к оплате с учетом скидки:', price - discount)