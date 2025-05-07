# Programa para verificar se um número é primo

# Recebe um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é menor ou igual a 1
if n <= 1:
    print("não primo")
else:
    # Verifica se há algum divisor entre 2 e n-1
    for i in range(2, n):
        if n % i == 0:
            print("não primo")
            break
    else:
        print("primo")

# Explicação:
# Um número é primo se:
# 1. É maior que 1
# 2. Não tem divisores além de 1 e ele mesmo
# O loop verifica se existe algum número entre 2 e n-1 que divide n
# Se encontrar, não é primo
# Se não encontrar, é primo
