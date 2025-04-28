# Exercício 3: Dígito das dezenas
# Recebe um número inteiro e imprime o dígito das dezenas

numero = int(input('Digite um número inteiro: '))
dezena = (numero // 10) % 10
print(f'O dígito das dezenas é {dezena}')
