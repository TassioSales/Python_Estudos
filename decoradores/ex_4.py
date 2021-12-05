def master(funcao):
    def slave():
        print('Agora estou decorado')
        funcao()

    return slave


@master
def fala_oi():
    print("oi")


fala_oi()
