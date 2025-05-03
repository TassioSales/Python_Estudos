numero = int(input('Digite um número: '))

soma = 0

while numero > 0:
    soma += numero % 10  # Adiciona o último dígito à soma
    numero //= 10  # Remove o último dígito

print(f'A soma dos dígitos é {soma}.')
