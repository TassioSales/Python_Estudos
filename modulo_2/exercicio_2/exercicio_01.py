def funcao_1(num1, num2):
    soma = num1 + num2
    return soma


def funcao_2(func):
    return f"O valor da soma e {func}"


print(funcao_2(funcao_1(5, 6)))
print(funcao_2(funcao_1(8, 9)))
