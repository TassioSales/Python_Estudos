num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    soma = num1 + num2
    print(soma)
else:
    print("Não pude realizar a soma")