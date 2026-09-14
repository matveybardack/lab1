# Отчет по первой лабораторной работе "Ознакомление с ЯП Python"
## Задание 0
Есть словарь - города и их расположение на координатной сетке. Создать словарь - расстояний между всеми парами городов.

**Формула расстояния между двумя точками:**
$$
distance = \frac{(x_1 - x_2)^2 + (y_1-y_2)^2}{2}
$$
### Описание проделанной работы
Был создан цикл, в котором создается новая пара ключ-значения для инициализированного ранее словаря, для которой во вложенном цикле перебираются остальные города и для них создается вложенный словарь с парами `город-расстояние до него` .
```python
def city_distances(sites: dict) -> dict:
    distances = {}

    for city1 in sites:
        distances[city1] = {}
        for city2 in sites:
            if city1 != city2:
                x1, y1 = sites[city1]
                x2, y2 = sites[city2]
                distances[city1][city2] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return distances
```
### Результат
![Pasted image 20260907101944.png](img/Pasted%20image%2020260907101944.png)
## Задание 1
Найти площадь круга по его радиусу и определить, лежат ли заданные точки внутри этого круга, центр которого лежит в нулевых координатах.
Радиус круга: 42
Координаты точек: (23, 34), (30, 30)

**Формула круга**
$$
S = \pi*r^2
$$
**Формула графика круга с центром (0,0)**
$$
x^2 + y^2 <= r^2
$$
### Описание проделанной работы
Написана формула для получения площади круга по его радиусу и формула для определения принадлежности точки кругу.
```python
def square_circle(radius) -> float:
    return round(pi * radius ** 2, 4)

def is_contains(point: tuple) -> bool:
    distance = (point[0] ** 2 + point[1] ** 2)
    return distance <= radius ** 2
```
### Результат
![d](img/Pasted%20image%2020260907103434.png)
## Задание 2
Расставьте знаки операций "плюс", "минус", "умножение" и скобки между числами "1 2 3 4 5" так, чтобы получилось число "25".
### Описание проделанной работы
Мыслительный перебор?
> **Рассуждения:** очевидно, что без умножения 25 не получить, тогда попробуем вычитать из 25 по единице, а разность раскладывать на множители. Цель: получить вычитаемое из диапазона целых \[1; 5\], а множители из оставшихся. Также следует учесть, что при умножении на 1 число не изменится, и её можно отбрасывать в переборе по необходимости.
```python
result = lambda: 1 * (2 + 3 + 4 * 5)
```
### Результат
![Pasted image 20260907105008.png](img/Pasted%20image%2020260907105008.png)
## Задание 3
Есть строка с перечислением фильмов "Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее". Выведите на консоль с помощью индексации строки, последовательно:
- первый
- последний
- второй
- второй с конца
### Описание проделанной работы
Использованы строковые срезы.
```python
def films_in_order(index: int, movies: str) -> str:
    list_movies = movies.split(', ')
    return list_movies[index]
```
### Результат
![Pasted image 20260907105527.png](img/Pasted%20image%2020260907105527.png)
## Задание 4
Создать список своей семьи и список приблизительного роста их членов. Найти рост отца и сумму ростов всех членов семьи.
### Описание проделанной работы
Использован краткий цикл для перебора всех членов и нахождения суммарного роста.
```python
# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['мама', 'папа', 'брат', 'сестра', 'я']

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    ['мама', 165],
    ['папа', 180],
    ['брат', 175],
    ['сестра', 160],
    ['я', 170],
]

def family_member_height(member: str, family_height: list):
    for mem in family_height:
        if mem[0] == member:
            return mem[1]

total_family_height = lambda family_height: sum([member[1] for member in family_height])
```
### Результат
![Pasted image 20260907110446.png](img/Pasted%20image%2020260907110446.png)
## Задание 5
Есть список животных в зоопарке. Посадить медведя (bear) между львом и кенгуру, добавить птиц из списка birds в последние клетки зоопарка, убрать слона (elephant) из зоопарка, вывести на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
**Список животных:**
```python
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
```
### Описание проделанной работы
```python
# Посадите медведя (bear) между львом и кенгуру
zoo.insert(1, 'bear')
print(zoo)

# Добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)

# Уберите слона (elephant) из зоопарка
zoo.remove('elephant')
print(zoo)

# Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
print(f'Лев сидит в клетке номер {zoo.index("lion") + 1}')
print(f'Жаворонок сидит в клетке номер {zoo.index("lark") + 1}')
```
### Результат
![Pasted image 20260907110906.png](img/Pasted%20image%2020260907110906.png)
## Задание 6
Есть список и словарь песен группы Depeche Mode со временем звучания с точностью до долей минут. Распечатать общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean'. Распечатать общее время звучания трех других песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'.
```python
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
```
### Описание проделанной работы
Были созданы листы `songs` и `songs2` с названиями искомых песен, выполнен перебор списка и словаря в цикле со сравнением имен песен и листов с суммированием времени их звучания.
```python
songs = ['Halo', 'Enjoy the Silence', 'Clean']
songs2 = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']

def song_time_sum(song_arr: list, violator_songs) -> float:
    total_time = 0.0
    match violator_songs:
        case dict():
            return round(sum([violator_songs[song] for song in song_arr]), 3)
        case list():
            for song in violator_songs:
                if song[0] in song_arr:
                    total_time += song[1]
            return round(total_time, 3)
        case _:
            return total_time

```
### Результат
![Pasted image 20260907180132.png](img/Pasted%20image%2020260907180132.png)
## Задача 7
Есть зашифрованное сообщение. Нужно его расшифровать и вывести на консоль в удобочитаемом виде.
```python
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
```
### Описание проделанной работы
Были использованы строковые срезы и формат строка для вывода сообщения в консоль.
```python
def decoder(secret_mes: list) -> str:
    # Ключ к расшифровке:
    #   первое слово - 4-я буква (индекс 3)
    word1 = secret_mes[0][3]

    #   второе слово - буквы с 10 по 13, включительно (индексы 9:13)
    word2 = secret_mes[1][9:13]

    #   третье слово - буквы с 6 по 15, включительно, через одну (индексы 5:15:2)
    word3 = secret_mes[2][5:15:2]

    #   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке (индексы 7:13[::-1])
    word4 = secret_mes[3][7:13][::-1]

    #   пятое слово - буквы с 17 по 21, включительно, в обратном порядке (индексы 16:21[::-1])
    word5 = secret_mes[4][16:21][::-1]

    return f'{word1} {word2} {word3} {word4} {word5}'
```
### Результат
![Pasted image 20260907180515.png](img/Pasted%20image%2020260907180515.png)
## Задача 8
Даны 2 кортежа цветов. Требуется преобразовать их во множества и вывести в консоль:
1. все виды цветов
2. те, что лежат в обоих множествах
3. те, что лежат только в одном из двух множеств
```python
# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
```
### Описание проделанной работы
Для выполнения задания были использованы такие операции над множествами как объединение, пересечение и разность.
```python
all_flowers = lambda set1, set2: set1 | set2
#print(all_flowers(garden_set, meadow_set))

# Выведите на консоль те, которые растут и там и там
both = lambda set1, set2: set1 & set2
#print(both(garden_set, meadow_set))

# Выведите на консоль те, которые растут в саду, но не растут на лугу
only_garden = lambda set1, set2: set1 - set2
#print(only_garden(garden_set, meadow_set))

# Выведите на консоль те, которые растут на лугу, но не растут в саду
only_meadow = lambda set1, set2: set2 - set1
```
### Результат
![Pasted image 20260907181206.png](img/Pasted%20image%2020260907181206.png)
## Задача 9
Есть словарь магазинов с распродажами. Требуется для каждого товара найти 2 магазина с минимальными ценами.
```python
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
```
### Описание проделанной работы
Словарь с ключом `магазин` был преобразован в словарь с ключом `товар`, списки из словарей были отсортированы по возрастанию цены, а затем обрезаны до двух первых словарей.
```python
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
```
### Результат
![Pasted image 20260907181908.png](img/Pasted%20image%2020260907181908.png)
## Задача 10
Есть словарь кодов товаров и словарь списков количества товаров на складе. Требуется рассчитать на какую сумму лежит каждого товара на складе.
**Формула стоимости по кол-ву и цене:**
$$
total\_cost = \sum_{i = 1}^n quantity_i \times price_i
$$
```python
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
```
### Описание проделанной работы
Выполнен перебор словаря с выводом на экран имени товара и итоговой стоимости.
```python
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
```
### Результат
![Pasted image 20260907182920.png](img/Pasted%20image%2020260907182920.png)
# Medium
## Описание проделанной работы
Создан верхнеуровневый модуль `main` в папке medium, куда были импортированы все модули из пакета rare. Файлы были переименованы для корректного импорта (имя модуля не может начинаться с цифр).
```python
import sys
from pathlib import Path
# Добавляем корень проекта в sys.path для корректного импорта
sys.path.append(str(Path(__file__).parent.parent))

# z ytyfdb;e gbnjy
# import rare

from rare.distance import sites, city_distances
from rare.circle import square_circle, is_contains
from rare.operations import result
from rare.favorite_movies import my_favorite_movies, films_in_order
from rare.my_family import family_member_height, total_family_height, my_family_height
from rare.zoo import final_zoo
from rare.songs_list import songs, songs2, song_time_sum, violator_songs_list, violator_songs_dict
from rare.secret import secret_message, decoder
from rare.garden import garden, meadow, all_flowers, both, only_garden, only_meadow
from rare.shopping import shops, products_min_price
from rare.store import goods, store, total_price_per_good

print('circle')
# circle
print(square_circle(42))
print(is_contains((23, 34)))
print(is_contains((30, 30)), end='\n\n')

print('distance')
# distance
print(city_distances(sites), end='\n\n')

print('operations')
# operations
print(result(), end='\n\n')

print('favorite_movies')
# favorite_movies
print(films_in_order(0, my_favorite_movies))
print(films_in_order(-1, my_favorite_movies))
print(films_in_order(1, my_favorite_movies))
print(films_in_order(-2, my_favorite_movies), end='\n\n')

print('garden')
# garden
print(all_flowers(set(garden), set(meadow)))
print(both(set(garden), set(meadow)))
print(only_garden(set(garden), set(meadow)))
print(only_meadow(set(garden), set(meadow)), end='\n\n')

print('my_family')
# my_family
print(family_member_height('папа', my_family_height))
print(total_family_height(my_family_height), end='\n\n')

print('secret')
# secret
print(decoder(secret_message), end='\n\n')

print('shopping')
# shopping
print(products_min_price(shops), end='\n\n')

print('song_lists')
# songs_list
print(song_time_sum(songs, violator_songs_list))
print(song_time_sum(songs2, violator_songs_dict), end='\n\n')

print('store')
# store
print(total_price_per_good(goods, store), end='\n\n')

print('zoo')
# zoo
print(f'Лев сидит в клетке номер {final_zoo.index("lion") + 1}')
print(f'Жаворонок сидит в клетке номер {final_zoo.index("lark") + 1}')
```
## Результат
![alt text](/img/image.png)
# Well-done
Для каждого модуля были написаны исчерпывающие тесты, покрывающие его функциональность
![alt text](/img/image%20copy.png)
# Шпаргалка по работе с git
- `git init` - создать проект в текущей директории
- `git commit <"сообщение коммита">` - создание коммита
- `git remote add origin <https://github.com:name/some.git>` - создать удаленный репозиторий
- `git push` - отправка изменений из локального репозитория в удаленный
# Ссылки на используемые ресурсы
1. [Справка по markdown](https://doka.guide/tools/markdown/)
2. [Официальный Python tutorial](https://docs.python.org/3/tutorial/)