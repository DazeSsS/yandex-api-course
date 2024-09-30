import requests
import pprint

# Вывести всех пользователей
response = requests.get('https://fakestoreapi.com/users')
users = response.json()
pprint.pp(users)
