def menu():
    # Exibe o menu de operações disponíveis
    print("""
    1 - Soma
    2 - Subtracao
    3 - Multiplicacao
    4 - Divisao
    """)

    while True:
        try:
            # Solicita que o usuário escolha uma opção
            opcao = int(input("Escolha uma opcao (1-4): "))
            # Verifica se a opção está dentro do intervalo válido
            if opcao in (1, 2, 3, 4):
                return opcao
            else:
                print("Erro: Opção inválida. Por favor, escolha um número entre 1 e 4.")
        except ValueError:
            # Trata o erro se a entrada não for um número inteiro
            print("Erro: Opção inválida. Por favor, digite um número inteiro.")


def obter_numeros():
    # Função para solicitar dois números ao usuário
    while True:
        try:
            # Solicita o primeiro número
            num1 = float(input("Digite o primeiro número: "))
            # Solicita o segundo número
            num2 = float(input("Digite o segundo número: "))
            return num1, num2
        except ValueError:
            # Trata o erro se a entrada não for um número válido
            print("Erro: Por favor, digite números válidos.")


def soma(num1, num2):
    # Função para somar dois números
    return num1 + num2


def subtracao(num1, num2):
    # Função para subtrair dois números
    return num1 - num2


def multiplicacao(num1, num2):
    # Função para multiplicar dois números
    return num1 * num2


def divisao(num1, num2):
    # Função para dividir dois números
    if num2 == 0:
        # Verifica se o divisor é zero e imprime uma mensagem de erro
        print("Erro: Divisão por zero não é permitida.")
        return None
    return num1 / num2


def main():
    # Função principal que executa o programa
    while True:
        # Exibe o menu e obtém a opção do usuário
        opcao = menu()
        # Obtém os números do usuário
        num1, num2 = obter_numeros()

        # Executa a operação escolhida pelo usuário
        if opcao == 1:
            print(f"Resultado: {soma(num1, num2)}")
        elif opcao == 2:
            print(f"Resultado: {subtracao(num1, num2)}")
        elif opcao == 3:
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif opcao == 4:
            resultado = divisao(num1, num2)
            if resultado is not None:
                print(f"Resultado: {resultado}")

        # Pergunta se o usuário deseja continuar
        esc = input("Deseja continuar? [S/N]: ").lower().strip()
        if esc == "n":
            print("Encerrando o programa.")
            break
        elif esc != "s":
            # Trata a resposta inválida do usuário
            print("Erro: Resposta apenas [S/N]")


if __name__ == "__main__":
    # Chama a função principal quando o script é executado
    main()
