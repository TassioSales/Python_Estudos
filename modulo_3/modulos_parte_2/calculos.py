from math import pi as PI
from random import randint


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


def gera_lista_dez_numeros():
    lista = []
    for c in range(1, 10):
        lista.append(randint(1, 100))
    return lista


