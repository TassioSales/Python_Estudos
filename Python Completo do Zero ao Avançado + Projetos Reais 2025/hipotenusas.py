def eh_hipotenusa(h):
    """
    Verifica se um número h é hipotenusa de algum triângulo retângulo com lados inteiros.
    Retorna True se for, False caso contrário.
    """
    # Verifica se h² pode ser escrito como soma de dois quadrados
    h_quadrado = h * h
    
    # Itera sobre possíveis catetos i e j
    # i pode ir até h-1 (pois j deve ser pelo menos 1)
    for i in range(1, h):
        i_quadrado = i * i
        # j pode ir até a raiz de (h² - i²)
        j_max = int((h_quadrado - i_quadrado) ** 0.5) + 1
        for j in range(1, j_max + 1):
            if i_quadrado + j * j == h_quadrado:
                return True
    return False

def soma_hipotenusas(n):
    """
    Soma todos os números entre 1 e n que são hipotenusas de triângulos retângulos com lados inteiros.
    Cada número é contado apenas uma vez, mesmo que seja hipotenusa de múltiplos triângulos.
    """
    soma = 0
    # Conjunto para armazenar as hipotenusas já encontradas
    hipotenusas_encontradas = set()
    
    # Verifica cada número de 1 até n
    for h in range(1, n + 1):
        if eh_hipotenusa(h) and h not in hipotenusas_encontradas:
            soma += h
            hipotenusas_encontradas.add(h)
    
    return soma

def main():
    """
    Função principal para testar as funções.
    """
    print("Soma das Hipotenusas")
    print("====================")
    
    try:
        n = int(input("Digite um número inteiro positivo: "))
        if n < 1:
            print("Por favor, digite um número positivo.")
            return
            
        resultado = soma_hipotenusas(n)
        print(f"A soma das hipotenusas até {n} é: {resultado}")
        
        # Mostra as hipotenusas encontradas (opcional)
        print("\nHipotenusas encontradas:")
        for h in range(1, n + 1):
            if eh_hipotenusa(h):
                print(f"- {h}")
                
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
