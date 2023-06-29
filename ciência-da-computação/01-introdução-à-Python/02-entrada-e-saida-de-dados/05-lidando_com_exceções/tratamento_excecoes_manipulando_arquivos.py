try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # será executado caso haja uma exceção
    print("Arquivo inexistente")
else:
    # será executado se tudo ocorre bem no try
    print("Arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir o arquivo")


# O with é a palavra reservada para gerenciamento de contexto. Este
# gerenciamento (with) é utilizado para encapsular a utilização de
# um recurso, garantindo que certas ações sejam tomadas independentemente
# se ocorreu ou não um erro naquele contexto.

# Criamos um contexto, limitando o escopo onde o arquivo está aberto.
# O uso do "as" aqui é somente para atribuir o valor utilizado no contexto
# à variável file
with open("arquivo.txt", "w") as file:
    file.write("Michelle 27\n")
# como estamos fora do contexto, o arquivo foi fechado
print(file.closed)
