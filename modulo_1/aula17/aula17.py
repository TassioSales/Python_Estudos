contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    contador += 1
    acumulador += contador
    if contador > 5:
        break
else:
    print("cheguei no else")
print("Isso sera execultado")