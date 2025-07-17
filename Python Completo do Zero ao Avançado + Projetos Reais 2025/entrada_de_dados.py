def dados_pessoais():
    """
    Função para coletar dados pessoais do usuário.
    Retorna um dicionário com os dados coletados.
    """
    dados = {}
    # Coleta de nome, idade, telefone,pais onde nasceu, altura e peso
    dados['nome'] = input("Digite seu nome: ")
    dados['idade'] = int(input("Digite sua idade: "))
    dados['telefone'] = input("Digite seu telefone: ")
    dados['pais_nascimento'] = input("Digite o país onde nasceu: ")
    dados['altura'] = float(input("Digite sua altura (em metros): "))
    dados['peso'] = float(input("Digite seu peso (em quilogramas): "))
    return dados

def imc (altura, peso):
    """
    Função para calcular o Índice de Massa Corporal (IMC).
    Recebe altura em metros e peso em quilogramas.
    Retorna o IMC calculado.
    """
    try:
        imc = 0
        situacao = ""
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
    except ValueError as e:
        print(f"Erro ao calcular IMC: {e}")
        return None, None
    except Exception as e:
        print(f"Erro ao calcular IMC: {e}")
        return None, None
    
def exibir_dados(dados):
    """
    Função para exibir os dados pessoais do usuário.
    Recebe um dicionário com os dados.
    """
    try:
        print("\nDados Pessoais Coletados:")
        print(f"Nome: {dados['nome']}")
        print(f"Idade: {dados['idade']} anos")
        print(f"Telefone: {dados['telefone']}")
        print(f"País de Nascimento: {dados['pais_nascimento']}")
        print(f"Altura: {dados['altura']} metros")
        print(f"Peso: {dados['peso']} kg")
        
        # Cálculo do IMC
        imc_valor, situacao = imc(dados['altura'], dados['peso'])
        if imc_valor is not None:
            print(f"IMC: {imc_valor:.2f} - Situação: {situacao}")
    except Exception as e:
        print(f"Erro ao exibir dados: {e}")
        return None, None   
    return imc_valor, situacao

def main():
    """
    Função principal que executa o programa.
    """
    try:
        dados = dados_pessoais()
        imc_valor, situacao = exibir_dados(dados)
    except Exception as e:
        print(f"Erro na execução do programa: {e}")
        return None, None   
    return imc_valor, situacao

if __name__ == "__main__":
    main()
