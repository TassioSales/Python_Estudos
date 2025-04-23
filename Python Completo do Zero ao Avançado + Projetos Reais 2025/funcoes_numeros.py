"""
funcoes_numeros.py

Este módulo demonstra funções básicas para números em Python:
- abs(x): valor absoluto
- round(x, ndigits): arredondamento
- divmod(a, b): quociente e resto
- pow(x, y[, z]): potência (com módulo opcional)
- int(x), float(x), complex(a, b): conversões de tipo
- sum(iterable): soma dos elementos
- min(), max(): valor mínimo e máximo

Também funções do módulo math:
- math.sqrt(x)
- math.ceil(x), math.floor(x)
- math.factorial(n)
"""
import math

def main():
    x = -7.5
    print(f"abs({x}) = {abs(x)}")
    print(f"round({x}) = {round(x)}")
    print(f"round(2.6789, 2) = {round(2.6789, 2)}")

    a, b = divmod(17, 3)
    print(f"divmod(17, 3) = (quociente={a}, resto={b})")

    print(f"pow(2, 5) = {pow(2, 5)}")
    print(f"pow(2, 5, 3) = {pow(2, 5, 3)}")

    print(f"int(3.9) = {int(3.9)}")
    print(f"float('3.14') = {float('3.14')}" )
    print(f"complex(2, 3) = {complex(2, 3)}")

    numbers = [1, 2, 3, 4, 5]
    print(f"sum({numbers}) = {sum(numbers)}")
    print(f"min({numbers}) = {min(numbers)}, max({numbers}) = {max(numbers)}")

    print(f"math.sqrt(16) = {math.sqrt(16)}")
    print(f"math.ceil(2.3) = {math.ceil(2.3)}, math.floor(2.7) = {math.floor(2.7)}")
    print(f"math.factorial(5) = {math.factorial(5)}")

if __name__ == "__main__":
    main()
