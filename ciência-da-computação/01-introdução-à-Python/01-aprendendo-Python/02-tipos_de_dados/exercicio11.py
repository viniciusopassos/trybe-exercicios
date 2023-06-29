# Realizar a contagem de quantas vezes cada elemento aparece em uma sequência é uma técnica muito útil na solução de alguns problemas. Qual é a estrutura mais recomendada para o armazenamento desta contagem?

my_array = [20, 20, 1, 2]

freq_dict = {}

for num in my_array:
    freq_dict[num] = freq_dict.get(num, 0) + 1 # o método get caso a chave num ñ exista no dict vai retornar o valor padrão que no caso é zero se existir add mais 1

for key, valor in freq_dict.items():
    print(f"{key} : {valor}")