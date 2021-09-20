l1 = [x for x in range(1, 10)]
l2 = [variavel*2 for variavel in l1]
l3 = [v ** 2 for v in l1]
l4 = [(v, v2) for v in l1 for v2 in range(3)]
l5 = ['Tassio', "Julia", "Lucas", "Cassio"]
l6 = [v.replace('a', "@") for v in l5]
l7 = [v.replace("a", "@").upper() for v in l5]
tp1 = (
    ("chave", "valor"),
    ("chave2", "valor2")
)
l8 = [(x, y) for x, y in tp1]
l9 = [(x, y) for y, x in tp1]
l10 = [v for v  in l2 ]

dict1 = dict(l9)

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)
print(l7)
print(l8)
print(l9)
print(dict1)