carrinho = []

carrinho.append(("Produto 1", 10))
carrinho.append(("Produto 2", 30))
carrinho.append(("Produto 3", 15))
carrinho.append(("Produto 4", 100))
carrinho.append(("Produto 5", 25))


def imprime_lista(produto, valor):
        print(f"O {produto} tem o valor {valor}")


for v in carrinho:
    imprime_lista(v[0], v[1])


soma_valor = sum(float(valor) for produto, valor in carrinho)
print(soma_valor)

