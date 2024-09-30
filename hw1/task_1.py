import requests
import pprint

# Вывести продукты, цена которых <20
response = requests.get('https://fakestoreapi.com/products')
products = response.json()

for product in products:
    if product.get('price') < 20:
        pprint.pp(product)
