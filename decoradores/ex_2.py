def master():
    def slave():
        print("oi")

    return slave


variavel = master()

variavel()

