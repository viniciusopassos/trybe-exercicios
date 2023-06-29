# lista completa de exceções:
# https://docs.python.org/pt-br/3/library/exceptions.html#bltin-exceptions

# Já as exceções ocorrem durante a execução e resultam em mensagem de erro.
# Veja exemplos de exceções:

print(10 * (1 / 0))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
print(4 + spam * 3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'spam' is not defined
print('2' + 2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
