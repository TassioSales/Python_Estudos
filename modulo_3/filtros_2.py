from dados import produtos, lista, pessoas

nova_lista = filter(lambda x: x > 5, lista)
lista_produto = filter(lambda p: p["preco"] > 50, produtos)

print(list(lista_produto))
print(list(nova_lista))


def filtra(produto):
    if produto["preco"] > 80:
        produto["E_caro"] = True
    return True


def filtro_pessoa(pessoas):
    if pessoas['idade'] > 18:
        return True


nova_lista_dois = filter(filtra, produtos)
nova_lista_tres = filter(filtro_pessoa, pessoas)

for produto  in nova_lista_dois:
    print(produto)

print()

for pessoa in nova_lista_tres:
    print(pessoa)
