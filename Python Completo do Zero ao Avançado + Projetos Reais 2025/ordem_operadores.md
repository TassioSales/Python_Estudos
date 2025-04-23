# Ordem de Precedência de Operadores em Python

Este documento apresenta a **ordem de avaliação** dos operadores em Python, da maior para a menor precedência.

| Precedência | Operadores                            | Descrição                         |
|-------------|----------------------------------------|-----------------------------------|
| 1           | `()`                                   | Parênteses                         |
| 2           | `**`                                  | Exponenciação                     |
| 3           | `+x`, `-x`, `~x`                      | Unários (positivo, negativo, bitwise NOT) |
| 4           | `*`, `/`, `//`, `%`                   | Multiplicação, divisão, divisão inteira, módulo |
| 5           | `+`, `-`                              | Adição e subtração                |
| 6           | `>>`, `<<`                            | Deslocamento de bits              |
| 7           | `&`                                   | AND bit a bit                     |
| 8           | `^`                                   | XOR bit a bit                     |
| 9           | ``                              | OR bit a bit                      |
| 10          | `<`, `<=`, `>`, `>=`, `==`, `!=`      | Comparações                       |
| 11          | `not x`                               | Negação lógica                    |
| 12          | `and`                                 | AND lógico                        |
| 13          | `or`                                  | OR lógico                         |
| 14          | `lambda`                              | Expressão lambda                  |

---

Exemplos:

```python
# 1) Parênteses alteram a ordem:
result = (2 + 3) * 4  # = 20 (sem parênteses seria 2 + (3*4) = 14)

# 2) Exponenciação é direita-associativa:
a = 2 ** 3 ** 2  # = 2 ** (3**2) = 2 ** 9 = 512

# 3) Unários antes de binários:
x = -3**2  # interpretado como -(3**2) = -9

# 4) Combinação de lógica e comparação:
a = 5 > 2 and 3 < 4  # True e True => True
b = not 0  # True, pois 0 é False em contexto booleano
```

> **Dica:** Para evitar ambiguidades, use parênteses sempre que a expressão ficar complexa.
