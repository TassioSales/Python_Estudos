def eh_primo(numero):
    """
    Verifica se um número é primo.
    Retorna True se for primo, False caso contrário.
    """
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    
    # Verifica divisores ímpares até a raiz quadrada do número
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

def n_primos(n):
    """
    Conta quantos números primos existem entre 2 e n (inclusive).
    """
    if n < 2:
        return 0
    
    contador = 0
    for numero in range(2, n + 1):
        if eh_primo(numero):
            contador += 1
    
    return contador

# Testes da função
def main():
    print("Testes da função n_primos:")
    print("n_primos(2) =", n_primos(2))     # Deve retornar 1 (apenas o número 2)
    print("n_primos(4) =", n_primos(4))     # Deve retornar 2 (2 e 3)
    print("n_primos(10) =", n_primos(10))   # Deve retornar 4 (2, 3, 5, 7)
    print("n_primos(20) =", n_primos(20))   # Deve retornar 8 (2, 3, 5, 7, 11, 13, 17, 19)
    
    # Teste interativo
    try:
        n = int(input("\nDigite um número inteiro maior ou igual a 2: "))
        if n < 2:
            print("Por favor, digite um número maior ou igual a 2.")
        else:
            qtd_primos = n_primos(n)
            print(f"Existem {qtd_primos} números primos entre 2 e {n}.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
