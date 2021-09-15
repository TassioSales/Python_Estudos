"""
iniciar com letra, pode conter números, separa _, letras minusculas
"""

nome = "Tassio"
sobrenome = "Sales"
idade = 31
e_maior = idade >= 18
altura = 1.83
peso = 92
imc = peso / (altura * altura)

print(f"Nome: {nome} {sobrenome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print(f"Peso: {peso}")
print(f"E maior de idade: {e_maior}")


print("***IMC****")
print(f"Seu IMC e {imc:.2f}")