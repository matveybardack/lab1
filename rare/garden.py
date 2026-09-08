# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# Создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

# Выведите на консоль все виды цветов
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
#print(only_meadow(garden_set, meadow_set))