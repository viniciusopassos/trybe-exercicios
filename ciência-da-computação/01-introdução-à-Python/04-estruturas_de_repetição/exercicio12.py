#  O Fatorial de um número inteiro é representado pela multiplicação de todos
# os números predecessores maiores que 0. Por exemplo, o fatorial de 5 é 120
# pois 5! = 1 * 2 * 3 * 4 * 5. Escreva um código que calcule o fatorial
# de um número inteiro.

fatorial = 1
for index in range(1, 6):
    fatorial = fatorial * index

print(fatorial)

# ---------------------------------------------

number = 5
counter = 1
result = 1

while counter <= number:
    result = result * counter
    counter += 1
print(result)

# ---------------------------------------------

number = 5
result = 1
# Usamos number + 1 pro range ir até o number
for factor in range(1, number+1):
    result *= factor
print(result)
