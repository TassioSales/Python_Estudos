def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f"oi {nome}"


def saudacao(nome, saudacao):
    return f"{saudacao} {nome}"


execultando = mestre(fala_oi, "Luiz")
execultando2 = mestre(saudacao, "Luiz ", saudacao= "BOM DIA")
print(execultando)
print(execultando2)