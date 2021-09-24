from itertools import count

contador = count()

lista = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q"]

lista = zip(contador, lista)

print(list(lista))
