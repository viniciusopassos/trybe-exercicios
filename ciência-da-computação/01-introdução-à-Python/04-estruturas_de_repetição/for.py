# filtragem de restaurantes percorrendo a lista e criando uma nova lista 
# com aquele restaurantes que atendem ao filtro

restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

filtered_restaurants = []
min_rating = 3.0
for restaurant in restaurants:
    if restaurant["nota"] >= min_rating:
        filtered_restaurants.append(restaurant)
# print(type(filtered_restaurants))
print(filtered_restaurants)


# em alguns casos percorreremos uma sequência numérica, para isso podemos 
# iterar o 'range'

for index in range(5):
    print(index)
