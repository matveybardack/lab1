import sys
from pathlib import Path
# Добавляем корень проекта в sys.path для корректного импорта
sys.path.append(str(Path(__file__).parent.parent))

from rare.store import goods, store, total_price_per_good

def test_total_price_per_good():
    result = ['Лампа - 27 шт, стоимость 1134 руб', 'Стол - 54 шт, стоимость 27860 руб', 'Диван - 3 шт, стоимость 3550 руб', 'Стул - 105 шт, стоимость 10311 руб']
    assert total_price_per_good(goods, store)  == result