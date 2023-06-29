nums = input("Informe os números separados por espaço: ")

nums_arr = nums.split(" ")
print(nums_arr)

sum = 0

for num in nums_arr:
    if not num.isdigit:
        print(f"Erro ao somar valores, {num} é um valor inválido")
    else:
        sum += int(num)

print(f"A soma dos valores é {sum}")
