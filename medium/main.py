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