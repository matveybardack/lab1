# Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

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