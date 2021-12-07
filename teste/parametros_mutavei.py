def lista_de_clientes(clientes_iteraveis, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteraveis)
    return lista


clientes1 = lista_de_clientes(["Joao", 'Maria', "Jose", 'Raimunto'])
clientes2 = lista_de_clientes(["Ricardo", "Fernando", "Tassio", "Paulo"])
clientes3 = lista_de_clientes(["Josemar"])

print(clientes1)
print(clientes2)
print(clientes3)
