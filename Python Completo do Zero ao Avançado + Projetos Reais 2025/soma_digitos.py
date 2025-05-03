n = int(input("Digite um número inteiro: "))
soma = 0
while n > 0:
    soma += n % 10
    n //= 10
print(soma)