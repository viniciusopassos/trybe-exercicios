# list comprehension

restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

min_rating = 3.0
filtered_restaurants = [
    restaurant['name']
    for restaurant in restaurants
    if restaurant["nota"] > min_rating
]
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D

# ---------------------------------------------------------------------------

# criar uma nova lista de strings com os nomes que contém a letra ‘a’.

names_list = ['Duda', 'Rafa', 'Cris', 'Yuri']
new_names_list = [name for name in names_list if 'a' in name]

print(new_names_list)

# --------------------------------------------------------------------------

# compreensão de listas para criar uma lista com o quadrado dos números entre 1 e 10.

quadrados = [x*x for x in range(11)]
print(quadrados)