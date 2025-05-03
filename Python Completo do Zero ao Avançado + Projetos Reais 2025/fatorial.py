n = int(input("Digite o valor de n: "))
if n < 0:
    print("Número inválido, fatorial é definido apenas para números naturais")
elif n == 0:
    print(1)
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(fatorial)