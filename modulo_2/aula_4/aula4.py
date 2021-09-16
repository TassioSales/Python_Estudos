variavel = "valor"  # escopo global

def func():
    print(variavel)


def func2(args=None):
    args = args.replace("v", "c")
    return args


func()
outra_variavel = func2(args=variavel)
print(outra_variavel)
