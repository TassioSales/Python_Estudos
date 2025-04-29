# Exercício 1 - Distância entre dois pontos
import math
x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))
distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
if distancia >= 10:
    print("longe")
else:
    print("perto")
