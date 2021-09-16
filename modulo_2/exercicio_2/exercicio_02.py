def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 + num2


def mulplica_resultado(func1, func2):
    return f"RESULTADO = {func1 * func2}"
    
    
print(mulplica_resultado(soma(8, 8), subtracao(50, 30)))


somar = soma(5,5)
sub = subtracao(10, 3)

print((mulplica_resultado(somar, sub)))