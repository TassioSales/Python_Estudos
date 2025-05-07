n = int(input("Digite o valor de n: "))
if n <= 0:
    print("Número inválido")
else:
    for i in range(1, 2*n, 2):
        print(i)