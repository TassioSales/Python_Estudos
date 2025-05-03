# Programa para imprimir os n primeiros números ímpares naturais usando while

# Recebe um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Inicializa as variáveis
numero = 1  # Começa com o primeiro número ímpar
contador = 0  # Contador de números ímpares impressos

# Loop while para imprimir os n primeiros números ímpares
while contador < n:
    print(numero)
    numero += 2  # Pula para o próximo número ímpar
    contador += 1  # Incrementa o contador

# Exemplo de saída para n = 5:
# 1
# 3
# 5
# 7
# 9
