base = int(input('Qual o número base? '))
limite = int(input('Até quanto deve ser multiplicado? '))

i = 1
while i <= limite:
    resultado = base * i
    print(f'{base} x {i} = {resultado}')
    i += 1
