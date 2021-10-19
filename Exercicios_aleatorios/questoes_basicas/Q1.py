# faça um programa que peça dois numeros inteiros e imprima a soma dos dois numeros:

def soma(num1, num2):
    soma_num = num1 + num2
    return soma_num


while True:
    num1 = input("Digite o primeiro numero: ")
    num2 = input("Digite outro numero: ")

    try:
        num1 = int(num1)
        num2 = int(num2)
        resultado = soma(num1, num2)
        print(resultado)
        try:
            esc = input("Deseja continuar ? [S/N]").lower().strip()[0]
            if esc == "n":
                break
            elif esc == "s":
                continue
            else:
                print("Erro apenas [Sim/Não]")
        except:
            print("Erro")
    except:
        print("Erro")
