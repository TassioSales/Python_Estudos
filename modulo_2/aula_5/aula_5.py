def funcao(arg, arg2):
    return arg * arg2


var = funcao(2, 2)

print(var)

a = lambda x, y: x * y

print(a(2, 2))

lista = [
    ["P1", 5],
    ["P2", 3],
    ["P3", 56],
    ["P4", 23],
    ["P5", 15]
]

lista.sort(key=lambda item: item[0], reverse=False)
print(lista)
print(sorted(lista, key=lambda i:i[0]))
