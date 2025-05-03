# Programa para calcular a soma dos dígitos de um número

# Recebe um número inteiro
numero = int(input("Digite um número inteiro: "))

# Inicializa a soma
soma = 0

# Loop while para somar os dígitos
while numero > 0:
    digito = numero % 10  # Pega o último dígito
    soma += digito  # Adiciona o dígito à soma
    numero = numero // 10  # Remove o último dígito

# Imprime o resultado
print(f"A soma dos dígitos é: {soma}")
