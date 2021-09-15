def division(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


divide = division(6, 2)

if divide:
    print(f"{divide:.2f}")
else:
    print("Conta invalida")
