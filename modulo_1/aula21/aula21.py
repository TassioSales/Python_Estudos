variaveis = ["Tassio", "Lucian", "Jesus", "Sales"]

for nome in variaveis:
    if nome.startswith("J"):
        print("Começa com J")
    else:
        print("não começa com J")

for valor in variaveis:
    if valor.lower().startswith("J"):
        pass
    print(valor)
else:
    print("não existe palavra com J")