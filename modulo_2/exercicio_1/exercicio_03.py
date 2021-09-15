"""
Crie uma função que receba 2 numeros. o primeiro e uam valor e o segundo um percetual. retorne
o valor do primeiro numero somado do aumento do persentual do mesmo.
"""

def soma_persentual(valor, porsentagem):
    adiciona_persentual = valor + (valor * porsentagem / 100)
    return adiciona_persentual


valor = soma_persentual(100, 100)
print(f"Resultado = {valor}")
