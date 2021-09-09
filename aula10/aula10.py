"""
operadores relacionais
>,<,==, , >=, <=, !=
"""

print(2 == 2)
print(2 >= 2)
print(2 == 1)

num1 = 2
num2 = 2
num3 = 3

print(num1, num2)

print(num1 == num2)
print(num1 > num2)
print(num1 >= num2)
print(num1 <= num3)
expressao = num1 == num2

print(expressao)
nome = input("Qual seu nome ? ")
idade = input("qual sua idade: ")
idade_limite = 18
idade = int(idade)

if idade >= idade_limite:
    print("Voce pode pegar o emprestimo")
else:
    print("Voce ainda nao tem idade suficiente par adquirir um emprestimo ")
