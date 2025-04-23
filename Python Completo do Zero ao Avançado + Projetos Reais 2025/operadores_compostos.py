"""
operadores_compostos.py

Este módulo demonstra o uso de operadores de atribuição composta em Python.
Estes operadores aplicam uma operação e atribuem o resultado na mesma expressão:

+=   soma e atribui
-=   subtrai e atribui
*=   multiplica e atribui
/=   divide e atribui (float)
//=  divide inteira e atribui
%=   módulo e atribui
**=  exponenciação e atribui
&=   E bit a bit e atribui
|=   OU bit a bit e atribui
^=   XOR bit a bit e atribui
>>=  desloca bits à direita e atribui
<<=  desloca bits à esquerda e atribui
"""

def main():
    x = 10
    print(f"Inicial x = {x}")

    x += 5
    print(f"x += 5 -> {x}")

    x -= 3
    print(f"x -= 3 -> {x}")

    x *= 2
    print(f"x *= 2 -> {x}")

    x /= 4
    print(f"x /= 4 -> {x}")

    x //= 2
    print(f"x //= 2 -> {x}")

    x %= 3
    print(f"x %= 3 -> {x}")

    x **= 4
    print(f"x **= 4 -> {x}")

    # para operadores bitwise precisamos de inteiro
    y = 0b1010  # 10 em binário
    print(f"Inicial y (bin) = {bin(y)}")

    y &= 0b1100
    print(f"y &= 0b1100 -> {bin(y)}")

    y |= 0b0011
    print(f"y |= 0b0011 -> {bin(y)}")

    y ^= 0b0110
    print(f"y ^= 0b0110 -> {bin(y)}")

    y >>= 2
    print(f"y >>= 2 -> {bin(y)}")

    y <<= 3
    print(f"y <<= 3 -> {bin(y)}")

if __name__ == "__main__":
    main()
