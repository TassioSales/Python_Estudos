# Programa para verificar se um número tem dígitos adjacentes iguais

# Recebe um número inteiro
numero = int(input("Digite um número inteiro: "))

# Inicializa variáveis
anterior = numero % 10  # Pega o último dígito
numero = numero // 10   # Remove o último dígito
encontrou = False  # Flag para indicar se encontrou dígitos adjacentes iguais

# Loop while para verificar os dígitos
while numero > 0 and not encontrou:
    atual = numero % 10  # Pega o próximo dígito
    if atual == anterior:  # Verifica se é igual ao dígito anterior
        encontrou = True
    else:
        anterior = atual  # Atualiza o dígito anterior
        numero = numero // 10  # Remove o dígito atual

# Imprime o resultado
if encontrou:
    print("sim")
else:
    print("não")

# Exemplos:
# 12345 -> não (nenhum dígito adjacente igual)
# 123445 -> sim (os dois 4 são adjacentes)
# 112345 -> sim (os dois 1 são adjacentes)
