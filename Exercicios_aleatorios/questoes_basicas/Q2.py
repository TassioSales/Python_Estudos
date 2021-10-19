# Escreva um programa que leia um valor em metros e o exiba convertido em milimetros, aceita virgula na entrada
# usuario

def converso_para_milimetros(centimetros):
    milimetros = centimetros * 1000
    return milimetros


while True:
    try:
        centimentro = float(input("Digite o valor em cm que deseja transforma para milimetro:"))
        resultado = converso_para_milimetros(centimentro)
        print(resultado)
    except Exception as E:
        print(E)
        print(E.__class__)
    else:
        break
