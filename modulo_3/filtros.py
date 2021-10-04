from dados import produtos,lista, pessoas

nova_lista = filter(lambda x: x > 5, lista)
lista_produto = filter(lambda p: p["preco"] > 50, produtos)

print(list(lista_produto))
print(list(nova_lista))


def filtra(produto):
    if produto["preco"] > 50:
        produto["Ecaro "]