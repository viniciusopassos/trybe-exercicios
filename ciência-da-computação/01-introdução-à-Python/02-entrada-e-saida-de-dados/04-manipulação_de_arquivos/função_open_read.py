#  Outro motivo importante para se fechar os arquivos é que normalmente
#  a manipulação de arquivos é feita através de buffers. Ou seja,
#  a escrita em disco pode não ser imediata. Quando fechamos o arquivo,
#  garantimos que tudo aquilo que ainda não está escrito seja persistido.

# A leitura do conteúdo de um arquivo pode ser feita utilizando a função read.
#  Para experimentar, vamos escrever em um arquivo e lê-lo logo em seguida!

# escrita
file = open("arquivo.txt", mode="w")
file.write("Trybe S2")
file.close()

# leitura
file = open("arquivo.txt", mode="r")
content = file.read()
print(content)
file.close()  # não podemos esquecer de fechar o arquivo

# Um arquivo é também um iterável, ou seja, pode ser percorrido em um laço
# de repetição. A cada iteração, uma nova linha é retornada. Vamos fazer
# igual ao exemplo anterior, porém dessa vez vamos escrever mais de uma linha!

# escrita
file = open("arquivo.txt", mode="w")
LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
file.writelines(LINES)
file.close()

# leitura
file = open("arquivo.txt", mode="r")
for line in file:
    print(
        line
    )  # não esqueça que a quebra de linha também é um caractere da linha
file.close()  # não podemos esquecer de fechar o arquivo
