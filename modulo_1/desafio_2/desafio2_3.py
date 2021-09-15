"""
Faça um programa que peça o nome do usuario. Se o nome tiver 4 letras ou menos escreva "Seu nome e curto"; se tiver
entre 5 e 6 letras, escreva "Seu nome e normal";maior que 6 escreva "Seu nome e muito grande"
"""

nome = input("Digite seu primeiro nome: ")

if len(nome) <= 4:
    print("Seu nome e curto")
elif len(nome) > 4:
    print("Seu nome e muito grande")