lista = [
    ("chave","valor"),
    ("chave_2","valor_2")
]

d1 = {f"chave_{x}": x ** 2 for x in range(5)}

print(d1)