def dados_pessoais() -> dict:
    """
    Coleta dados pessoais do usuário com validação.
    Retorna um dicionário com os dados coletados.
    """
    dados = {}
    dados['nome'] = input("Digite seu nome: ")
    while True:
        try:
            dados['idade'] = int(input("Digite sua idade: "))
            if dados['idade'] <= 0:
                raise ValueError
            break
        except ValueError:
            print("Idade inválida. Digite um número inteiro positivo.")
    dados['telefone'] = input("Digite seu telefone: ")
    dados['pais_nascimento'] = input("Digite o país onde nasceu: ")
    while True:
        try:
            dados['altura'] = float(input("Digite sua altura (em metros): "))
            if dados['altura'] <= 0:
                raise ValueError
            break
        except ValueError:
            print("Altura inválida. Digite um número positivo.")
    while True:
        try:
            dados['peso'] = float(input("Digite seu peso (em quilogramas): "))
            if dados['peso'] <= 0:
                raise ValueError
            break
        except ValueError:
            print("Peso inválido. Digite um número positivo.")
    return dados

def calcular_imc(altura: float, peso: float) -> tuple[float, str]:
    """
    Calcula o Índice de Massa Corporal (IMC) e retorna o valor e a situação.
    """
    if altura <= 0 or peso <= 0:
        raise ValueError("Altura e peso devem ser maiores que zero.")
    imc = peso / (altura ** 2)
    if imc < 18.5:
        situacao = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        situacao = "Peso normal"
    elif 25 <= imc < 29.9:
        situacao = "Sobrepeso"
    elif 30 <= imc < 34.9:
        situacao = "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        situacao = "Obesidade grau 2"
    else:
        situacao = "Obesidade grau 3"
    return imc, situacao

def exibir_dados(dados: dict) -> None:
    """
    Exibe os dados pessoais do usuário.
    """
    print("\nDados Pessoais Coletados:")
    print(f"Nome: {dados['nome']}")
    print(f"Idade: {dados['idade']} anos")
    print(f"Telefone: {dados['telefone']}")
    print(f"País de Nascimento: {dados['pais_nascimento']}")
    print(f"Altura: {dados['altura']} metros")
    print(f"Peso: {dados['peso']} kg")

def main() -> None:
    """
    Função principal que executa o programa.
    """
    try:
        dados = dados_pessoais()
        exibir_dados(dados)
        imc_valor, situacao = calcular_imc(dados['altura'], dados['peso'])
        print(f"IMC: {imc_valor:.2f} - Situação: {situacao}")
    except Exception as e:
        print(f"Erro na execução do programa: {e}")

if __name__ == "__main__":
    main()
