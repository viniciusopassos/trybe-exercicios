# Crie uma variável do tipo lista chamada lista_frutas contendo
# os valores "banana", "uva", "maça", "pera"

lista_frutas = ["banana", "uva", "maça", "pera"]

# utilize um laço "for" para imprimir a primeira letra da string
for fruta in lista_frutas:
    print(fruta[0])

# utilize um laço "for" para imprimir a quarta letra da string
for fruta in lista_frutas:
    print(fruta[3])  # vai gerar um erro IndexError (objetivo do exercício)
# pois a string uva não tem a quarta letra
