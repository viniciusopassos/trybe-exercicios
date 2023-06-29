input("Digite uma mensagem: ")  # exemplo de entrada de dados com a função
# input


import random  # importar o módulo random


# escolhe um número aleatório entre 1 e 10
random_number = random.randint(1, 10)
guess = ""

# enquanto não adivinhar o número
while guess != random_number:
    # pergunte a pessoa usuária um número
    guess = int(input("qual o seu palpite entre os números 1 e 10? "))

print("O número sorteado era:", guess)
