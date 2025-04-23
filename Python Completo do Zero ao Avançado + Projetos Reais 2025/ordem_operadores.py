"""
ordem_operadores.py

Este script exibe a ordem de precedência de operadores em Python e exemplos demonstrativos.
"""

def main():
    # Tabela de precedência (do maior para o menor)
    precedences = [
        (1, '()', 'Parênteses'),
        (2, '**', 'Exponenciação'),
        (3, '+x, -x, ~x', 'Unários (positivo, negativo, bitwise NOT)'),
        (4, '*, /, //, %', 'Multiplicação, divisão, divisão inteira, módulo'),
        (5, '+, -', 'Adição e subtração'),
        (6, '>>, <<', 'Deslocamento de bits'),
        (7, '&', 'AND bit a bit'),
        (8, '^', 'XOR bit a bit'),
        (9, '|', 'OR bit a bit'),
        (10, '<, <=, >, >=, ==, !=', 'Comparações'),
        (11, 'not x', 'Negação lógica'),
        (12, 'and', 'AND lógico'),
        (13, 'or', 'OR lógico'),
        (14, 'lambda', 'Expressão lambda')
    ]

    print("ORDEM DE PRECEDÊNCIA DE OPERADORES EM PYTHON")
    for level, ops, desc in precedences:
        print(f"{level:2}. {ops:20} - {desc}")

    print("\nEXEMPLOS:")
    # 1) Parênteses
    result = (2 + 3) * 4
    plain = 2 + 3 * 4
    print(f"1) (2 + 3) * 4 = {result}  (sem parênteses: 2 + (3*4) = {plain})")

    # 2) Exponenciação é direita-associativa
    a = 2 ** 3 ** 2
    print(f"2) 2 ** 3 ** 2 = {a}")

    # 3) Unários antes de binários
    x = -3**2
    print(f"3) -3**2 = {x}  (equivale a -(3**2))")

    # 4) Combinação de lógica e comparação
    b1 = 5 > 2 and 3 < 4
    b2 = not 0
    print(f"4) 5 > 2 and 3 < 4 = {b1}")
    print(f"5) not 0 = {b2}")

if __name__ == "__main__":
    main()
