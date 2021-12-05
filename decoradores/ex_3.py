def master(funcao):
    def slave():
        funcao()

    return slave


def fala_oi():
    print("oi")


variavel = master(fala_oi)

variavel()
