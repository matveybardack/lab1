import sys
from pathlib import Path
# Добавляем корень проекта в sys.path для корректного импорта
sys.path.append(str(Path(__file__).parent.parent))

from rare.my_family import family_member_height, total_family_height, my_family_height

def test_father_height():
    assert family_member_height('папа', my_family_height) == 180

def test_total_family_height():
    assert total_family_height(my_family_height) == 850