try:
    a = 1 / 0
except NameError as N:
    print(N)
    print(N.__class__)
    print("Erro de definição do nome da variavel")
except (IndexError, KeyError) as I:
    print(I)
    print(I.__class__)
    print("Erro de indice")
except Exception as E:
    print(E)
    print(E.__class__)
    print("Erro")
else:
    pass
finally:
    a = " "
print(a)
