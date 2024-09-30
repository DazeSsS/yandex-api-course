import requests
import pprint

# Вывести все продукты с категорией  "jewelery"
response = requests.get('https://fakestoreapi.com/products/category/jewelery')
jewelery = response.json()
pprint.pp(jewelery)
