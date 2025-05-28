def calcular_fatorial(n):
    """
    Calcula o fatorial de um número inteiro não negativo.
    Retorna 1 se n for 0.
    """
    if n == 0 or n == 1:
        return 1
    return n * calcular_fatorial(n - 1)

def main():
    """
    Função principal que lê um número do usuário e exibe seu fatorial.
    """
    print("Cálculo de Fatorial")
    print("===================")
    
    while True:
        try:
            numero = int(input("\nDigite um número inteiro não negativo (ou um número negativo para sair): "))
            
            if numero < 0:
                print("Programa encerrado.")
                break
                
            resultado = calcular_fatorial(numero)
            print(f"O fatorial de {numero} é {resultado}")
            
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
