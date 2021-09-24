from itertools import zip_longest, count

cidades = ["São paulo", "Belo Horizonte", "Salvador", "Monte Belo", "Taguatinga"]
estados = ["SP", "MG", "BA"]

indice = count()
cidades_estados = zip(
    indice,
    estados,
    cidades,
    # fillvalue="Estado"
)

for indice, cidades, estados in cidades_estados:
    print(indice, cidades, estados)