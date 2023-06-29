file = open("_notas.txt", mode="r")
for line in file:
    listLine = line.split()
    if int(listLine[1]) < 6:
        print(listLine[0])
