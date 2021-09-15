"""
Faça um programa que peça o horario para o usuario e digite, bom dia ,boa tarde e ,boa noite
"""


hora = input("Digite a hora atual: ")[0:2]
print(hora)

hora = int(hora)

if 1 <= hora <= 12:
    print("BOM DIA")
elif 13 <= hora <= 18:
    print("BOA TARDE")
else:
    print("BOA NOITE")