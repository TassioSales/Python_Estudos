"""
operadores logicos
and, or, not, in, not in
"""


nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))


idade_menor = 18
idade_maior = 30

if idade_menor <= idade <= idade_maior:
    print("Pode pegar o emprestimos")
else:
    print('Nâo pode pehgar o emprestimos')


a = 2
b = 3

if not b > a:
    print("b e maior que a")
else:
    print('a e maior que b')


nome = "Tassio Sales"

if "Sales" in nome:
    print("Existe")
else:
    print("Não Existe")