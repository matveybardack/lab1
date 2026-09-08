# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.
# Каждый товар может лежать в нескольких местах (партиях) с разной ценой.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# и вывести в формате
#   <товар> - <кол-во> шт, стоимость <сумма> руб

# Перебираем каждый товар
#for good_name, code in goods.items():
#    total_quantity = 0
#    total_cost = 0
#    
#    # Находим все партии этого товара на складе
#    if code in store:
#        for batch in store[code]:
#            quantity = batch['quantity']
#            price = batch['price']
#            total_quantity += quantity
#            total_cost += quantity * price
#    
#    print(f'{good_name} - {total_quantity} шт, стоимость {total_cost} руб')

# medium
def total_price_per_good(goods: dict, store: dict) -> list:
    list_total_price = []

    for good_name, code in goods.items():
        total_quantity = 0
        total_cost = 0

        # Находим все партии этого товара на складе
        if code in store:
            for batch in store[code]:
                quantity = batch['quantity']
                price = batch['price']
                total_quantity += quantity
                total_cost += quantity * price

        list_total_price.append(f'{good_name} - {total_quantity} шт, стоимость {total_cost} руб')

    return list_total_price