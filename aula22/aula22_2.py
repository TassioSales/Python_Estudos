teste = "O rato roeu a ropa do rei de roda - tres pratos de trigo para tres tigres tristes"
lista = teste.split(" ")

for index, valor in enumerate(lista):
    print(index, valor, lista[index])

print("\n")

lista_1 = [
    [1, "Luiz"],
    [3, "João"],
    [5, "Maria"]
]
for v in lista_1:
    print(v)

print()

for index, valor in lista_1:
    print(index, valor)
