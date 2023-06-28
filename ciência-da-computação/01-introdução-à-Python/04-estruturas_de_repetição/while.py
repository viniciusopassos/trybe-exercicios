# sequência de Fibonacci (sequência numérica começando por 0 e 1)

n = 10
last, next = 0 ,1
while last < n:
    print(last)
    last, next = next, last + next 