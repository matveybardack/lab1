# Есть словарь магазинов с распродажами

shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99}
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99}
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99}
    ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
# sweets = {
#     'печенье': [
#         {'shop': 'пятерочка', 'price': 9.99},
#         {'shop': 'ашан', 'price': 10.99},
#     ],
#     ...
# }
# Указать надо только по 2 магазина с минимальными ценами

#sweets = {}
#
## Собираем все продукты
#products = {}
#for shop_name, items in shops.items():
#    for item in items:
#        product_name = item['name']
#        price = item['price']
#        if product_name not in products:
#            products[product_name] = []
#        products[product_name].append({'shop': shop_name, 'price': price})
#
## Для каждого продукта выбираем 2 магазина с минимальными ценами
#for product_name, offers in products.items():
#    sorted_offers = sorted(offers, key=lambda x: x['price'])
#    sweets[product_name] = sorted_offers[:2]
#
#print(sweets)

# medium
def products_min_price(shops: dict) -> dict:
    sweets = {}

    # Собираем все продукты
    products = {}
    for shop_name, items in shops.items():
        for item in items:
            product_name = item['name']
            price = item['price']
            if product_name not in products:
                products[product_name] = []
            products[product_name].append({'shop': shop_name, 'price': price})

    # Для каждого продукта выбираем 2 магазина с минимальными ценами
    for product_name, offers in products.items():
        sorted_offers = sorted(offers, key=lambda x: x['price'])
        sweets[product_name] = sorted_offers[:2]

    return sweets