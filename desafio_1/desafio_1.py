"""
 * Criar variaveis para nome (str) e idade (int)
 * altura (float) e peso (float) de uma pessoa
 * Criar uma variavel com ano atual (int)
 * obter o ano de nascimento da pessoas (baseado na idade do ano atual)
 * Obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
 *Exibir todos os valores na tela usando F-string (com chaves)
"""
nome = "Tassio Lucian de jesus Sales"
altura = float(1.83)
peso = float(90)
anoAtual = 2021
anoNacimento = 1990
idade = anoAtual - anoNacimento
imc = peso / (altura * altura)

print(f"Nome: {nome} tipo: {type(nome)}")
print(f"Idade: {idade} tipo: {type(idade)}")
print(f"Peso: {peso} tipo: {type(peso)}")
print(f"Altura: {altura} tipo: {type(altura)}")
print(f"IMC: {imc:.2f} tipo: {type(imc)}")

