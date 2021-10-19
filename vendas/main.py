from vendas.calc_preco import aumenta, reducao
from vendas.formata import preco as rr

preco = 49.90

preco_com_aumento = aumenta(valor=preco, porcetagem=15, formata=True)
print(preco_com_aumento)
preco_com_reducao = reducao(valor=preco, porcetagem=15, formata=True)
print(preco_com_reducao)

print(rr.real(preco))
