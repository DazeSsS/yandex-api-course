import requests
import pprint

# Добавить пользователя со своим именем
response = requests.post(
    'https://fakestoreapi.com/users',
    data={
        'email': 'ivan@gmail.com',
        'username': 'ivan',
        'password': 'password',
        'name': {
            'firstname': 'Ivan',
            'lastname': 'Rakov'
        },
        'address': {
            'city': 'Yekaterinburg',
            'street': 'Pushkina dom Kolotushkina',
            'number': 10,
            'zipcode': '127612',
            'geolocation': {
                'lat': '12.3456',
                'long': '78.9012'
            }
        },
        'phone': '1234567890'
    }
)
new_user = response.json()
pprint.pp(new_user)
