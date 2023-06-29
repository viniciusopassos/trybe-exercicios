# Além de arquivos textuais (como os que manipulamos até agora), também
# existem arquivos binários. Eles são arquivos que contêm uma série de bytes
# e a sua leitura pode variar de acordo com o arquivo. Nesse caso, devemos
# acrescentar um b ao parâmetro mode, indicando que será utilizado o
# modo binário.

# As operações são similares a de um arquivo textual. Porém tanto a
#  escrita quanto a leitura devem ser feitas utilizando bytes.


# escrita
file = open("arquivo.dat", mode="wb")
file.write(b"C\xc3\xa1ssio 30")  # o prefixo b em uma string indica que
# seu valor está codificado em bytes
file.close()

# leitura
file = open("arquivo.dat", mode="rb")
content = file.read()
print(content)  # saída: b'C\xc3\xa1ssio 30'
file.close()  # não podemos esquecer de fechar o arquivo
