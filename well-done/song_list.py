import sys
from pathlib import Path
# Добавляем корень проекта в sys.path для корректного импорта
sys.path.append(str(Path(__file__).parent.parent))

from rare.songs_list import songs, songs2, song_time_sum, violator_songs_list, violator_songs_dict

def test_songs():
    assert song_time_sum(songs, violator_songs_list) == 14.93

def test_songs2():
    assert song_time_sum(songs2, violator_songs_dict) == 13.49