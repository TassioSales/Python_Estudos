from dados import produtos, pessoas, lista


def aumenta_preco(p):
    p["preco"] = round(p['preco'] * 1.05, 2)
    return p


def aumenta_idade(p):
    p["nova_idade"] = p["idade"] + 5
    return p


novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)

print(f"\n\n")

nomes = map(lambda p: p["nome"], pessoas)
nomes_2 = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)

print(f"\n\n")

for pessoa in nomes_2:
    print(pessoa)

