"""
Entrada de dados
"""

nome = str(input("Digite seu nome ? "))
idade = int(input("Qual sua idade ? "))

print(f"Alo! prazer em te conhecer {nome} o tipo da varivel e {type(nome)}")
print(f"Pelo que você informou você tem {idade} anos o tipo dessa variavel e {type(idade)}")


num1 = int(input("digite um numero: "))
num2 = input("digite outro numero: ")
num2 = int(num2)

print(num1 + num2)