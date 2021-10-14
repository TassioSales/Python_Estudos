def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as Erro:
        print(Erro)
        raise


try:
    print(divide(2, 0))
except:
    print("Erro")
