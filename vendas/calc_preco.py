from vendas.formata import preco


def aumenta(valor, porcetagem, formata=False):
    r = valor + (valor * porcetagem / 100)
    if formata:
        return preco.real(r)
    else:
        return r


def reducao(valor, porcetagem, formata=False):
    r = valor - (valor * porcetagem / 100)
    if formata:
        return preco.real(r)
    else:
        return r
