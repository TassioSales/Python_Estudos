"""
modulo_math.py

Este script apresenta de forma completa o módulo math do Python,
exibindo suas constantes, funções principais e exemplos de uso.
"""
import math

def main():
    # Função principal que demonstra o uso completo do módulo math
    # Imprime docstring e exemplos de constantes e funções
    # Descrição geral do módulo
    print("Módulo math:")
    print(math.__doc__)

    # ---- Constantes ----
    # Exibe constantes matemáticas padrão definidas no módulo
    print("\nConstantes:")
    print(f"pi = {math.pi}")
    print(f"e = {math.e}")
    print(f"tau = {math.tau}")
    print(f"inf = {math.inf}, nan = {math.nan}")

    # ---- Funções principais ----
    # Demonstra uso das principais funções do módulo math
    print("\nFunções principais:")

    # 1) sqrt(x) - calcula a raiz quadrada de x
    print("\n1. sqrt(x) - raiz quadrada de x")
    print(f"   sqrt(16) = {math.sqrt(16)}")

    # 2) ceil(x), floor(x) - valor inteiro mais próximo acima e abaixo
    print("\n2. ceil(x), floor(x) - teto e piso de x")
    print(f"   ceil(2.3) = {math.ceil(2.3)}, floor(2.7) = {math.floor(2.7)}")

    # 3) factorial(n) - calcula o fatorial de n
    print("\n3. factorial(n) - fatorial de n")
    print(f"   factorial(5) = {math.factorial(5)}")

    # 4) sin, cos, tan - operações trigonométricas em radianos
    print("\n4. sin(x), cos(x), tan(x) - funções trigonométricas (x em radianos)")
    print(f"   sin(pi/2) = {math.sin(math.pi/2)}, cos(0) = {math.cos(0)}, tan(pi/4) = {math.tan(math.pi/4)}")

    # 5) degrees, radians - converte entre graus e radianos
    print("\n5. degrees(x), radians(x) - conversão graus↔radianos")
    print(f"   degrees(pi) = {math.degrees(math.pi)}, radians(180) = {math.radians(180)}")

    # 6) exp, log - função exponencial e logaritmo com base opcional
    print("\n6. exp(x), log(x[, base]) - exponencial e logaritmo")
    print(f"   exp(1) = {math.exp(1)}, log(e) = {math.log(math.e)}, log(100, 10) = {math.log(100, 10)}")

    # 7) hypot - calcula hipotenusa dado dois catetos
    print("\n7. hypot(x, y) - hipotenusa (teorema de Pitágoras)")
    print(f"   hypot(3, 4) = {math.hypot(3, 4)}")

    # 8) comb, perm - combinatória e permutação de elementos
    print("\n8. comb(n, k), perm(n, k) - combinações e permutações")
    print(f"   comb(5, 2) = {math.comb(5, 2)}, perm(5, 2) = {math.perm(5, 2)}")

    # 9) fmod, trunc - resto da divisão IEEE e truncamento de floats
    print("\n9. fmod(x, y), trunc(x) - resto de divisão e truncamento")
    print(f"   fmod(17, 3) = {math.fmod(17, 3)}, trunc(3.9) = {math.trunc(3.9)}")

    # 10) gcd - calcula o maior divisor comum entre dois inteiros
    print("\n10. gcd(a, b) - máximo divisor comum")
    print(f"   gcd(24, 16) = {math.gcd(24, 16)}")

    # 11) copysign - aplica sinal de y ao valor absoluto de x
    print("\n11. copysign(x, y) - sinal de y aplicado a x")
    print(f"   copysign(3, -0.0) = {math.copysign(3, -0.0)}")

    # 12) isfinite, isinf, isnan - checagens de tipo numérico especial
    print("\n12. isfinite(x), isinf(x), isnan(x) - verificações numéricas")
    print(f"   isfinite(1e308) = {math.isfinite(1e308)}, isinf(1e400) = {math.isinf(1e400)}, isnan(math.nan) = {math.isnan(math.nan)}")

    # ---- Funções avançadas e especiais ----
    # 13) modf, remainder - separa parte inteira/fração e resto IEEE
    print("\n13. modf(x) - parte inteira e fração")
    print(f"   modf(3.5) = {math.modf(3.5)}")
    print("\n14. remainder(x, y) - resto IEEE 754")
    print(f"   remainder(17, 3) = {math.remainder(17, 3)}")

    # 15) frexp, ldexp - decompõe e reconstrói números em mantissa e expoente
    print("\n15. frexp(x), ldexp(m, e) - mantissa e expoente, reconstrução")
    print(f"   frexp(8) = {math.frexp(8)}, ldexp(0.5, 4) = {math.ldexp(0.5, 4)}")

    # 16) expm1, log1p - operações precisas para pequenos valores
    print("\n16. expm1(x), log1p(x) - exp(x)-1 e log(1+x)")
    print(f"   expm1(1) = {math.expm1(1)}, log1p(0.1) = {math.log1p(0.1)}")

    # 17) log2, log10 - logaritmos em bases 2 e 10
    print("\n17. log2(x), log10(x) - logaritmos base 2 e 10")
    print(f"   log2(8) = {math.log2(8)}, log10(100) = {math.log10(100)}")

    # 18) funções hiperbólicas - variações de sin, cos e tan
    print("\n18. Funções hiperbólicas: sinh, cosh, tanh")
    print(f"   sinh(0) = {math.sinh(0)}, cosh(0) = {math.cosh(0)}, tanh(0) = {math.tanh(0)}")

    # 19) funções especiais - gamma, lgamma, erros gaussiano
    print("\n19. Funções especiais: gamma, lgamma, erf, erfc")
    print(f"   gamma(5) = {math.gamma(5)}, lgamma(5) = {math.lgamma(5)}, erf(1) = {math.erf(1)}, erfc(1) = {math.erfc(1)}")

    # 20) isclose - comparação numérica com tolerâncias
    print("\n20. isclose(x, y[, rel_tol, abs_tol]) - comparação numérica")
    print(f"   isclose(0.1+0.2, 0.3) = {math.isclose(0.1+0.2, 0.3)}")

    # 21) prod - calcula produto de todos os elementos de um iterável
    print("\n21. prod(iterable) - produto dos elementos")
    print(f"   prod([1,2,3,4]) = {math.prod([1,2,3,4])}")

    # 22) dist - distância euclidiana entre dois pontos em n-dimensões
    print("\n22. dist(p, q) - distância euclidiana entre pontos")
    print(f"   dist((1,2),(4,6)) = {math.dist((1,2),(4,6))}")

    # 23) isqrt - raiz quadrada truncada para inteiro
    print("\n23. isqrt(n) - raiz quadrada inteira")
    print(f"   isqrt(17) = {math.isqrt(17)}")

if __name__ == "__main__":
    main()
