def somar_numeros():
    # Inicializa a soma com 0
    soma = 0
    
    while True:
        # Solicita um número ao usuário
        numero = int(input("Digite um número (0 para encerrar): "))
        
        # Se o usuário digitar 0, encerra o loop
        if numero == 0:
            break
            
        # Adiciona o número à soma
        soma += numero
        
        # Mostra a soma parcial
        print(f"Soma parcial: {soma}")
    
    # Exibe o resultado final
    print(f"\nA soma final dos números digitados é: {soma}")

# Executa a função
if __name__ == "__main__":
    somar_numeros()
