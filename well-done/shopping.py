import sys
from pathlib import Path
# Добавляем корень проекта в sys.path для корректного импорта
sys.path.append(str(Path(__file__).parent.parent))

from rare.shopping import shops, products_min_price

def test_products_min_price():
    result = {'печенье': [{'shop': 'пятерочка', 'price': 9.99}, {'shop': 'ашан', 'price': 10.99}], 'конфеты': [{'shop': 'магнит', 'price': 30.99}, {'shop': 'пятерочка', 'price': 32.99}], 'карамель': [{'shop': 'магнит', 'price': 41.99}, {'shop': 'ашан', 'price': 45.99}], 'пирожное': [{'shop': 'пятерочка', 'price': 59.99}, {'shop': 'магнит', 'price': 62.99}]}
    assert products_min_price(shops) == result