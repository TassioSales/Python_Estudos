def computador_escolhe_jogada(n, m):
    """
    Determina a jogada do computador usando a estratégia vencedora.
    Retorna o número de peças a serem retiradas.
    """
    # A estratégia é deixar múltiplos de (m+1) peças para o jogador
    pecas_retirar = n % (m + 1)
    if pecas_retirar == 0:
        # Se não for possível deixar múltiplo, tira o máximo possível
        return min(m, n)
    return pecas_retirar

def usuario_escolhe_jogada(n, m):
    """
    Solicita e valida a jogada do usuário.
    Retorna o número de peças a serem retiradas.
    """
    while True:
        try:
            jogada = int(input("\nQuantas peças você vai tirar? "))
            if 1 <= jogada <= m and jogada <= n:
                return jogada
            else:
                print(f"\nOops! Jogada inválida! Tente de novo.")
        except ValueError:
            print("\nPor favor, digite um número válido.")

def partida():
    """
    Executa uma partida do jogo NIM.
    """
    print("\n**** Rodada ****\n")
    
    # Solicita os parâmetros iniciais
    while True:
        try:
            n = int(input("Quantas peças? "))
            m = int(input("Limite de peças por jogada? "))
            if n > 0 and m > 0:
                break
            else:
                print("Os números devem ser maiores que zero.")
        except ValueError:
            print("Por favor, digite números válidos.")
    
    # Define quem começa
    computador_comeca = n % (m + 1) != 0
    
    if computador_comeca:
        print("\nComputador começa!")
    else:
        print("\nVocê começa!")
    
    # Loop principal do jogo
    while n > 0:
        if computador_comeca:
            # Vez do computador
            pecas = computador_escolhe_jogada(n, m)
            n -= pecas
            if pecas == 1:
                print(f"\nO computador tirou uma peça.")
            else:
                print(f"\nO computador tirou {pecas} peças.")
            
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "computador"
        else:
            # Vez do usuário
            pecas = usuario_escolhe_jogada(n, m)
            n -= pecas
            if pecas == 1:
                print("\nVocê tirou uma peça.")
            else:
                print(f"\nVocê tirou {pecas} peças.")
            
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                return "usuario"
        
        # Atualiza o tabuleiro
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        elif n > 1:
            print(f"Agora restam {n} peças no tabuleiro.")
        
        # Alterna o jogador
        computador_comeca = not computador_comeca

def campeonato():
    """
    Executa um campeonato com 3 partidas.
    """
    print("\nVoce escolheu um campeonato!")
    placar_computador = 0
    placar_usuario = 0
    
    for rodada in range(1, 4):
        print(f"\n**** Rodada {rodada} ****")
        vencedor = partida()
        if vencedor == "computador":
            placar_computador += 1
        else:
            placar_usuario += 1
    
    print("\n**** Final do campeonato! ****")
    print(f"\nPlacar: Você {placar_usuario} X {placar_computador} Computador")

def main():
    """
    Função principal que inicia o jogo.
    """
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    while True:
        try:
            opcao = int(input())
            if opcao == 1:
                partida()
                break
            elif opcao == 2:
                campeonato()
                break
            else:
                print("Opção inválida! Escolha 1 ou 2.")
        except ValueError:
            print("Por favor, digite 1 ou 2.")

if __name__ == "__main__":
    main()
