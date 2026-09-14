import sys
from pathlib import Path
# Добавляем корень проекта в sys.path для корректного импорта
sys.path.append(str(Path(__file__).parent.parent))

from rare.secret import secret_message, decoder

def test_decoder():
    result = 'в бане веник дороже денег'
    assert decoder(secret_message) == result