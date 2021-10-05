from dados import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
soma_idade = reduce(lambda ac, id: id["idade"] + ac, pessoas, 0)

print(soma_lista)
print(soma_preco)
print(soma_idade)
media = soma_idade / len(pessoas)
print(media)
