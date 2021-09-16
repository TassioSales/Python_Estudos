def func(*args, **kwargs):
    print(args)
    print(kwargs["nome"], kwargs["sobrenome"])

    idade = kwargs.get("idade")
    if idade is not None:
        print(idade)
    else:
        print("Idade não existe")


lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

func(*lista, *lista2, nome="Tassio", sobrenome="Sales", idade = "31")