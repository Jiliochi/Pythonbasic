lista = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], [0]
]
for index in lista:
    for jdex in index:
        print(jdex)

for index in range(4):
    for jdex in range(3):
        print(lista[index][jdex])