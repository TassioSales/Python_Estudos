def desenhar_retangulo_vazio(largura, altura):
    """
    Desenha um retângulo vazio com '#' apenas nas bordas.
    """
    for linha in range(altura):
        for coluna in range(largura):
            # Verifica se está na primeira/última linha ou primeira/última coluna
            if linha == 0 or linha == altura - 1 or coluna == 0 or coluna == largura - 1:
                print('#', end='')
            else:
                print(' ', end='')
        print()  # Pula para a próxima linha

def main():
    """
    Função principal que obtém as entradas do usuário e chama a função de desenho.
    """
    print("Desenho de Retângulo Vazio")
    print("==========================")
    
    try:
        # Obtém a largura e altura do usuário
        largura = int(input("Digite a largura: "))
        altura = int(input("Digite a altura: "))
        
        # Garante que os valores são positivos
        if largura <= 0 or altura <= 0:
            print("Por favor, digite valores maiores que zero.")
            return
            
        # Desenha o retângulo vazio
        desenhar_retangulo_vazio(largura, altura)
        
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    main()
