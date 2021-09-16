"""
funções
"""


def func(*args, **kwargs):
    return args

lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

concat = func(*lista, *lista2)

print(concat)