# Programa para calcular o fatorial de um número natural usando while

# Recebe um número natural do usuário
n = int(input("Digite um número natural: "))

# Inicializa as variáveis
fatorial = 1
contador = 1

# Calcula o fatorial usando um loop while
while contador <= n:
    fatorial *= contador
    contador += 1

# Imprime o resultado
print(f"O fatorial de {n} é {fatorial}")
