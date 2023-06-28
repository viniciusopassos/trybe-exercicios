# Percorra a lista do exercício 13 e imprima “Múltiplo de 3” se o elemento for divisível por 3.

ratings = [6, 8, 5, 9, 10]
result = [
    number
    for number in ratings
        if number % 3 == 0
]

print(f'{result} são multiplos de 3')

# ------------------------------------------------

result_list = [60, 80, 50, 90, 100]
new_list = [
    number
    for number in result_list
        if number % 3 == 0
]

print(f'{new_list} são multiplos de 3')


# ------------------------------------------------

ratings = [6, 8, 5, 9, 10]

for rating in ratings:
    # o sinal % representa a operação "resto".
    if (rating % 3) == 0: # se o resto é zero, é divisível
        print(f'{rating} é múltiplo de 3')