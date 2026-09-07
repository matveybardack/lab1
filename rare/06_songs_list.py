# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

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

# Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
songs = ['Halo', 'Enjoy the Silence', 'Clean']
total_time = 0
for song in violator_songs_list:
    if song[0] in songs:
        total_time += song[1]
print(f'Три песни звучат {round(total_time, 3)} минут')

# Есть словарь песен группы Depeche Mode
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

# Распечатайте общее время звучания трех других песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
songs2 = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
total_time2 = sum([violator_songs_dict[song] for song in songs2])
print(f'А другие три песни звучат {round(total_time2, 3)} минут')