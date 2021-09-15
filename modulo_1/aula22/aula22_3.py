lista = [
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I']
]

enumerada = list(enumerate(lista))

print(enumerada)

print(enumerada[1][1][0])

"""
[<-- Enumerate
 
    (0,['A','B','C']),
    (1,['D','E','F']),
    (2,['G','H','I'])
]
"""

for v1 in enumerate(lista):
    minha_lista = v1[1]
    letra1, letra2, letra3 = minha_lista
    print(minha_lista)
    print(letra1, letra2, letra3)