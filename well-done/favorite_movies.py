import sys
from pathlib import Path
# Добавляем корень проекта в sys.path для корректного импорта
sys.path.append(str(Path(__file__).parent.parent))

from rare.favorite_movies import my_favorite_movies, films_in_order

def test_films_in_order_first():
    result = "Терминатор"
    assert films_in_order(0, my_favorite_movies) == result

def test_films_in_order_last():
    result = "Пятый элемент"
    assert films_in_order(1, my_favorite_movies) == result

def test_films_in_order_second():
    result = "Назад в будущее"
    assert films_in_order(-1, my_favorite_movies) == result

def test_films_in_order_secondlast():
    result = "Чужие"
    assert films_in_order(-2, my_favorite_movies) == result