nome = "Tassio"
sobrenome = "Sales"
idade = 31
e_maior = idade >= 18
altura = 1.83
peso = 92
imc = peso / (altura * altura)


print(nome, "tem", idade, "idade e seu imc er", imc)
print("{} tem {} idade e seu imc e {:.2f}".format(nome, idade, imc))
print(f"{nome} tem {idade} idade e seu imc e {imc:.2f}")
