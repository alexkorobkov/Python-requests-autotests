import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers_by_level():

    """
    KTI-1. Get trainers by level
    """
    response = requests.get(url=f'{URL}/trainers', params={'level': 1}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

CASES = [
    (4714,'Salavat','Alex'),
    (4657, 'Moscow','Serge')
]

@pytest.mark.parametrize('id, city, trainer_name', CASES)

def test_get_trainers_by_id():

    """
    KTI-2. Get trainers by id
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 4714}, timeout=5)
    assert response.json()['city'] == 'Salavat', ''
    assert response.json()['trainer_name'] == 'Alex', ''
    assert response.status_code == 200, 'Unexpected status code'

    





