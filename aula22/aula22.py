string = "O Braisl e o pais do futebol, o Brasil e penta"

lista = string.split(" ")
lista2 = string.split(",")

palavra = " "
contagem = 0

for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f"A palavra que apareceu mais vezes e {palavra} ({contagem})")

teste = "O rato roeu a ropa do rei de roda - tres pratos de trigo para tres tigres tristes"

lista = teste.split(" ")
teste2 = ",".join(lista)

print(teste)
print(lista)
print(teste2)
