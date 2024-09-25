import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "LOGIN",
    "password": "PASSWORD"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазав",
    "photo_id": 1
}
rename_pokemon = {
    "pokemon_id": "72734",
    "name": "Буба",
    "photo_id": 2
}
catch_pokemon = {
    "pokemon_id": "72734"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''
'''response_creat =  requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create) 
print(response_creat.text)
print(response_creat.status_code)
message = response_creat.json()['message']
print(message)'''
'''response_catch_pokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch_pokemon)
print(response_catch_pokemon.text)'''
response_rename_pokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = rename_pokemon)
print(response_rename_pokemon.text)
