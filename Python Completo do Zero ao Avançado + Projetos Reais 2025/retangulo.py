def desenhar_retangulo(largura, altura):
    """
    Desenha um retângulo com '#' baseado na largura e altura fornecidas.
    """
    for _ in range(altura):  # Para cada linha da altura
        for _ in range(largura):  # Para cada coluna da largura
            print('#', end='')  # Imprime '#' sem quebrar a linha
        print()  # Pula para a próxima linha após preencher a largura

def main():
    """
    Função principal que obtém as entradas do usuário e chama a função de desenho.
    """
    print("Desenho de Retângulo")
    print("====================")
    
    try:
        # Obtém a largura e altura do usuário
        largura = int(input("Digite a largura: "))
        altura = int(input("Digite a altura: "))
        
        # Garante que os valores são positivos
        if largura <= 0 or altura <= 0:
            print("Por favor, digite valores maiores que zero.")
            return
            
        # Desenha o retângulo
        desenhar_retangulo(largura, altura)
        
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    main()
