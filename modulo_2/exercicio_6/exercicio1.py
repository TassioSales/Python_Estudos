lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_c = zip(lista_a, lista_b)
lista_d = []
for num in lista_c:
    lista_d.append(sum(num))

print(lista_d)


lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)