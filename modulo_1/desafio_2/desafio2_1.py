"""
Faça um programa que peça ao usuario para digitar um numero inteiro, informe ao usuario se esse numero a par ou impar
Caso o usuario nao digite um numero inteiro deixo uma menssagem informando que nao e um numero inteiro
"""

num = input("Digite um numero: ")

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")
else:
    print("Não e possivel converter o numero")

