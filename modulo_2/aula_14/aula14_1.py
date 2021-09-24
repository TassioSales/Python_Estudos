from itertools import count

contador = count(start=5, step=-1)

for valor in contador:
    print(f'{valor: .2f}')
    if valor >= 1000 or valor <= -1000:
        break
