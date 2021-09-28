from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', "nota": "A"},
    {'nome': 'Maria', "nota": "B"},
    {'nome': 'Paulo', "nota": "C"},
    {'nome': 'Ricardo', "nota": "B"},
    {'nome': 'Tassio', "nota": "A"},
    {'nome': 'Julia', "nota": "C"},
    {'nome': 'Lucas', "nota": "B"},
    {'nome': 'Joana', "nota": "B"},
    {'nome': 'Cassio', "nota": "A"},
    {'nome': 'Jose', "nota": "A"},
    {'nome': 'Marcos', "nota": "A"},
]
ordenar = lambda item: item["nota"]
alunos.sort(key=ordenar)
alunos_agrupados = groupby(alunos, ordenar)

for agrupamento, valores_agrupado in alunos_agrupados:
    va1, va2 = tee(valores_agrupado)
    print(f"Agrupamento: {agrupamento}")

    for alunos in va1:
        print(f'\t{alunos}')

    qtd =  len(list(va2))
    print(f"\t{qtd} alunos tiraram a nota {agrupamento}")
    print()