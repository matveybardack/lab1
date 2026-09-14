import sys
from pathlib import Path
# Добавляем корень проекта в sys.path для корректного импорта
sys.path.append(str(Path(__file__).parent.parent))

from rare.circle import square_circle, is_contains

def test_square_circle():
    assert square_circle(42) == 5541.7693

def test_is_contains_true():
    assert is_contains((23, 34))

def test_is_contains_false():
    assert not is_contains((30, 30))