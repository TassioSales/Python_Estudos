def decompor_em_primos(n):
    """
    Decompõe um número em seus fatores primos.
    Retorna uma lista com os fatores primos em ordem crescente.
    """
    if n < 2:
        return [n]
        
    fatores = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            fatores.append(divisor)
            n = n // divisor
        divisor += 1
        
        # Otimização: se divisor² for maior que n e n for maior que 1, 
        # então n é primo e não precisa mais ser dividido
        if divisor * divisor > n and n > 1:
            fatores.append(n)
            break
            
    return fatores

def formatar_decomposicao(fatores):
    """
    Formata a lista de fatores primos em uma string legível.
    Exemplo: [2, 2, 3, 5] -> "2 × 2 × 3 × 5"
    """
    if not fatores:
        return "1"
    return " × ".join(map(str, fatores))

def main():
    """
    Função principal que lê um número do usuário e exibe sua decomposição em primos.
    """
    print("Decomposição em Fatores Primos")
    print("=============================")
    
    while True:
        try:
            entrada = input("\nDigite um número inteiro maior que 1 (ou 'sair' para encerrar): ")
            
            if entrada.lower() == 'sair':
                print("Encerrando o programa...")
                break
                
            numero = int(entrada)
            
            if numero < 2:
                print("Por favor, digite um número inteiro maior que 1.")
                continue
                
            fatores = decompor_em_primos(numero)
            resultado = formatar_decomposicao(fatores)
            
            print(f"{numero} = {resultado}")
            
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro ou 'sair'.")

if __name__ == "__main__":
    main()
