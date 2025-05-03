numero = input('Digite um número: ')
soma = 0
indice = 0
while indice < len(numero):
    soma += int(numero[indice])
    indice += 1

print(f'A soma dos dígitos de {numero} é {soma}.')
