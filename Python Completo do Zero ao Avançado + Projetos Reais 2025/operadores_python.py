"""
operadores_python.py

Este módulo explica os principais operadores disponíveis em Python, com exemplos de uso.
"""

# Operadores Aritméticos
# +  Adição
# -  Subtração
# *  Multiplicação
# /  Divisão (resultado float)
# // Divisão inteira (floor)
# %  Módulo (resto da divisão)
# ** Exponenciação

# Operadores de Atribuição
# =   Atribuição simples
# +=  Soma e atribui
# -=  Subtrai e atribui
# *=  Multiplica e atribui
# /=  Divide e atribui
# //= Divide inteira e atribui
# %=  Módulo e atribui
# **= Exponenciação e atribui

# Operadores de Comparação
# ==  Igual a
# !=  Diferente de
# >   Maior que
# <   Menor que
# >=  Maior ou igual
# <=  Menor ou igual

# Operadores Lógicos
# and  Retorna True se ambos os operandos forem True
# or   Retorna True se ao menos um operando for True
# not  Inverte o valor lógico

# Operadores Bitwise (a nível de bits)
# &   E bit a bit
# |   OU bit a bit
# ^   OU exclusivo bit a bit
# ~   NOT bit a bit (complemento)
# <<  Deslocamento à esquerda
# >>  Deslocamento à direita

# Operadores de Membro
# in      True se elemento está em uma sequência
# not in  True se elemento não está em uma sequência

# Operadores de Identidade
# is      True se ambas variáveis apontam para o mesmo objeto
# is not  True se não apontam para o mesmo objeto


def main():
    # Exemplos de uso
    a, b = 10, 3

    print("Aritméticos:")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a} ** {b} = {a ** b}")

    print("\nAtribuição:")
    c = a
    print(f"c = {c}")
    c += b
    print(f"c += b -> {c}")

    print("\nComparação:")
    print(f"{a} == {b}? {a == b}")
    print(f"{a} != {b}? {a != b}")
    print(f"{a} > {b}? {a > b}")

    print("\nLógicos:")
    print(f"True and False -> {True and False}")
    print(f"True or False  -> {True or False}")
    print(f"not True      -> {not True}")

    print("\nBitwise:")
    print(f"{a} & {b} = {a & b}")
    print(f"{a} | {b} = {a | b}")
    print(f"{a} ^ {b} = {a ^ b}")
    print(f"~{a} = {~a}")
    print(f"{a} << 1 = {a << 1}")
    print(f"{a} >> 1 = {a >> 1}")

    print("\nMembro e Identidade:")
    seq = [1, 2, 3]
    print(f"2 in {seq}? {2 in seq}")
    print(f"4 not in {seq}? {4 not in seq}")
    x = seq
    y = seq.copy()
    print(f"x is seq? {x is seq}")
    print(f"y is seq? {y is seq}")

if __name__ == "__main__":
    main()
