# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

## Выведите на консоль с помощью индексации строки, последовательно:
##   первый фильм
#print(my_favorite_movies[:10])
#
##   последний
#print(my_favorite_movies[-15:])
#
##   второй
#print(my_favorite_movies[12:25])
#
##   второй с конца
#print(my_favorite_movies[-22:-17])

# medium
def films_in_order(index: int, movies: str) -> str:
    list_movies = movies.split(', ')
    return list_movies[index]