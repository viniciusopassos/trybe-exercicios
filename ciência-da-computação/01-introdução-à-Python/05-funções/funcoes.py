# posicional: são aqueles definidos por meio da posição em que cada um é passado;
# nomeada: são definidos por meio de seus nomes.


def soma(x, y):
    return x + y


print(soma(2, 2))  # os parâmetros aqui são posicionais

print(soma(x=2, y=2))  # aqui estamos nomeando os parâmetros

# ----------------------------------------------------------------------


def concat(*strings):
    # Equivalente a um ", ".join(strings), que concatena os elementos de um iterável em uma string utilizando um separador
    # Nesse caso a string resultante estaria separada por vírgula
    final_string = ""
    for string in strings:
        final_string += string
        if not string == strings[-1]:
            final_string += ", "
    return final_string


# pode ser chamado com 2 parâmetros
print(concat("Carlos", "Cristina"))  # saída: "Carlos, Cristina"

# pode ser chamado com um número n de parâmetros
print(
    concat("Carlos", "Cristina", "Maria")
)  # saída: "Carlos, Cristina, Maria"

# dict é uma função que já vem embutida no python
print(
    dict(nome="Felipe", sobrenome="Silva", idade=25)
)  # cria um dicionário utilizando as chaves passadas

print(
    dict(nome="Ana", sobrenome="Souza", idade=21, turma=1)
)  # o número de parâmetros passados para a função pode variar

# ----------------------------------------------------------------------

len([1, 2, 3, 4])  # função len não aceita argumentos nomeados

len(obj=[1, 2, 3, 4])  # este código irá falhar

print("Coin", "Rodrigo", ", ")  # imprime Coin Rodrigo ,

print(
    "Coin", "Rodrigo", sep=", "
)  # nomeando o terceiro parâmetro, agora temos a saída: Coin, Rodrigo
