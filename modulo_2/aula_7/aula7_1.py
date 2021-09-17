clientes = {
    "cliente1":{"nome":"Tassio",
                "Sobrenome":"Sales"},

    "cliente2":{"nome":"Rodrigo",
                "Sobrenome":"Maia"}

}

for cliente_k, cliente_v in clientes.items():
    print(f"Exibindo {cliente_k}")
    for dados_k, dados_v in cliente_v.items():
        print(f"\t{dados_k} = {dados_v}")


clientela = clientes.copy()
print(clientela)