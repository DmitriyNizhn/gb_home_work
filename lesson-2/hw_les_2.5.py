import random

amount_products = 13  # количество позиций
price_list = []  # Создаю список
for i in range(0, amount_products):
    price = round(random.random() * 1000, 2)
    price_list.append(price)
print(price_list)

for el in price_list[:amount_products - 1]:
    rub = int(el)
    cent = round(el % 1 * 100)
    print(f'{rub} руб {cent:02} коп', end=', ')
print(f'{int(price_list[amount_products - 1])} руб '
      f'{round(price_list[amount_products - 1] % 1 * 100)} коп')

price_list.sort()  # Отсортирован по возрастанию

for el in price_list[:amount_products - 1]:
    rub = int(el)
    cent = round(el % 1 * 100)
    print(f'{rub} руб {cent:02} коп', end=', ')
print(f'{int(price_list[amount_products - 1])} руб '
      f'{round(price_list[amount_products - 1] % 1 * 100)} коп')

print(price_list)  # Доказательство неизмености списка

new_price_list = price_list[:]  # Создан новый список
new_price_list.sort(reverse=True)  # отсортирован по убыванию

print(*((f'{int(el)} руб {round(el % 1 * 100):02} коп') for el in new_price_list[:5]))  # отсутствует ','
