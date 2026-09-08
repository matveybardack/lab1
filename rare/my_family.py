# Создайте списки:

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

## Выведите на консоль рост отца в формате
#for member in my_family_height:
#    if member[0] == 'папа':
#        print(f'Рост отца - {member[1]} см')
#
## Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#total_height = sum([member[1] for member in my_family_height])
#print(f'Общий рост моей семьи - {total_height} см')

# medium
def family_member_height(member: str, family_height: list):
    for mem in family_height:
        if mem[0] == member:
            return mem[1]

total_family_height = lambda family_height: sum([member[1] for member in family_height])