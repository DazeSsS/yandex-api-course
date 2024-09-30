import requests

# Вывести все категории
response = requests.get('https://fakestoreapi.com/products/categories')
categories = response.json()
print(categories)
