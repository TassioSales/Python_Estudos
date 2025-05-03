# Programa interativo para demonstrar o uso de booleanos em Python

print("Bem-vindo ao programa interativo de booleanos!")
print("=" * 50)

# 1. Verificador de idade
print("\n1. Verificador de idade")
idade = int(input("Digite sua idade: "))
maior_de_idade = idade >= 18
print(f"Você é maior de idade? {'Sim' if maior_de_idade else 'Não'}")
print(f"Idade válida para dirigir? {'Sim' if idade >= 16 else 'Não'}")

# 2. Verificador de número
print("\n2. Verificador de número")
numero = float(input("Digite um número: "))

# Várias verificações usando booleanos
positivo = numero > 0
par = numero % 2 == 0
inteiro = numero == int(numero)

print(f"O número é positivo? {'Sim' if positivo else 'Não'}")
print(f"O número é par? {'Sim' if par else 'Não'}")
print(f"O número é inteiro? {'Sim' if inteiro else 'Não'}")

# 3. Verificador de senha
print("\n3. Verificador de senha")
senha = input("Digite uma senha: ")

# Critérios para senha segura
min_caracteres = len(senha) >= 8
contem_maiuscula = any(c.isupper() for c in senha)
contem_minuscula = any(c.islower() for c in senha)
contem_numero = any(c.isdigit() for c in senha)

print("\nAnálise da senha:")
print(f"Tem pelo menos 8 caracteres? {'Sim' if min_caracteres else 'Não'}")
print(f"Contém letras maiúsculas? {'Sim' if contem_maiuscula else 'Não'}")
print(f"Contém letras minúsculas? {'Sim' if contem_minuscula else 'Não'}")
print(f"Contém números? {'Sim' if contem_numero else 'Não'}")

# 4. Jogo de adivinhação
print("\n4. Jogo de adivinhação")
numero_secreto = 42

while True:
    tentativa = int(input("Digite um número (1-100) ou 0 para sair: "))
    
    if tentativa == 0:
        print("Jogo encerrado!")
        break
        
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif tentativa < numero_secreto:
        print("Tente um número maior!")
    else:
        print("Tente um número menor!")

print("\nObrigado por usar o programa!")
