import pytest
from places_remember.models import Memory, Userpic


@pytest.mark.django_db
def test_Memory():
    memory = Memory()
    memory.author = 'Зульхия'
    memory.title = 'Воспоминания из детства'
    memory.comment = 'Это моё детство'

    assert memory.author == 'Зульхия'
    assert memory.title == 'Воспоминания из детства'
    assert memory.comment == 'Это моё детство'
