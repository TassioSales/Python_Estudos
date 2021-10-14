def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as V:
        try:
            valor = float(valor)
            return valor
        except ValueError as V:
            pass


while True:
    numero = converte_numero(input("Digite um numero: "))
    # if numero is not None:
    #     print(numero * 5)
    # else:
    #     print("Isso nao e um numero")
    #     continue
    if numero is None:
        print("Isso nao e um numero")
    else:
        print(numero * 5)