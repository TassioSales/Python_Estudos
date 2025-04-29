# PROGRAMA PARA CALCULAR AS RAÍZES DA EQUAÇÃO DO 2º GRAU (FÓRMULA DE BHÁSKARA)
# O programa pede os coeficientes a, b, c ao usuário, calcula o delta e mostra as raízes
# Também informa se as raízes são reais ou não

import math

print("=== Calculadora de Bhaskara ===")

# Entrada dos coeficientes
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

print(f"Equação: {a}x² + {b}x + {c} = 0")

# Calculando o delta
delta = b**2 - 4*a*c
print(f"Delta: {delta}")

if a == 0:
    print("Não é uma equação do 2º grau (a deve ser diferente de 0).")
elif delta < 0:
    print("As raízes não são reais (delta negativo).")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Primeira raiz: {raiz1}")
    print(f"Segunda raiz: {raiz2}")
    if delta == 0:
        print("As raízes são reais e iguais.")
    else:
        print("As raízes são reais e diferentes.")
