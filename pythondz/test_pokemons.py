import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'df8b8a069cfc0fd7eb7ef7a1f8765869'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '10453'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Буба'
def test_name_trainer():
    response_trainers = requests.get(url = f'{URL}/trainers?trainer_id=10453', headers = HEADER )
    assert response_trainers.json()["data"][0]["trainer_name"] == 'godpokengo'
@pytest.mark.parametrize('key, value', [('name', 'Буба'), ('trainer_id', TRAINER_ID), ('id', '72734')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
