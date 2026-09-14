import sys
from pathlib import Path
# Добавляем корень проекта в sys.path для корректного импорта
sys.path.append(str(Path(__file__).parent.parent))

from rare.garden import garden, meadow, all_flowers, both, only_garden, only_meadow

def test_all_flowers():
    result = {'подсолнух', 'ромашка', 'клевер', 'одуванчик', 'мак', 'роза', 'гладиолус'}
    assert all_flowers(set(garden), set(meadow)) == result

def test_both():
    result = {'ромашка', 'одуванчик'}
    assert both(set(garden), set(meadow)) == result

def test_only_garden():
    result = {'подсолнух', 'роза', 'гладиолус'}
    assert only_garden(set(garden), set(meadow)) == result

def test_only_meadow():
    result = {'мак', 'клевер'}
    assert only_meadow(set(garden), set(meadow)) == result