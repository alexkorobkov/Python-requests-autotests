import requests

URL = 'https://api.pokemonbattle.me:9104'

HEADER = {'Content-Type': 'application/json','trainer_token': 'c9c5e13468704716a1c4267471062c36'}

body = {
    "name": "clon",
   "photo": "https://dolnikov.ru/pokemons/albums/005.png"
}

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')
body = {
    "pokemon_id": "28370",
    "name": "kolya",
    "photo": "https://dolnikov.ru/pokemons/albums/005.png"
}

response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5 )
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')

body = {
    "pokemon_id": "28370"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')