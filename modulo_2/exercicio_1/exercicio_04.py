"""
Fizz Buzz - Se o parametro da função for divisilvelpor 2 retorne fizz
se o parametro da função for divisilvel por 5 retorne buzz se o parametro
da divisão for divisivel por 5 e por 3 retorne FizzBuzz caso contrario retorne o numero enviado
"""


def fizzbuzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz 3 "
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    return num


qtd = input("Quantos numeros deseja testa: ")
while not qtd.isnumeric():
    print("Erro o digite um numero:")
    qtd = input("Quantos numeros deseja testa: ")

qtd = int(qtd)

soma = 0
while soma < qtd:
    num = input("Digite uma numero: ")
    if not num.isnumeric():
        print("Digite apenas numeros")
        continue
    num = float(num)
    print(fizzbuzz(num))
    soma += 1
