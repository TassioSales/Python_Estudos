from Conta import Conta
from Cliente import Cliente

def main():
    """
    Função principal para testar a classe Conta e Cliente com diversas operações e cenários.
    """
    # Criação de um cliente
    cliente1 = Cliente(
        nome="João Silva",
        cpf="12345678901",
        data_nascimento="01/01/1980",
        sexo="M",
        estado_civil="Solteiro",
        profissao="Engenheiro",
        nacionalidade="Brasileiro",
        naturalidade="São Paulo",
        endereco="Rua A, 123",
        telefone="11999999999",
        email="joao@email.com"
    )

    # Criação de uma conta com titular Cliente
    conta1 = Conta(titular=cliente1, numero=12345, saldo=1000.0, limite=500.0)

    # Criação de outro cliente e conta
    cliente2 = Cliente(
        nome="Maria Souza",
        cpf="98765432100",
        data_nascimento="15/05/1990",
        sexo="F",
        estado_civil="Casada",
        profissao="Médica",
        nacionalidade="Brasileira",
        naturalidade="Rio de Janeiro",
        endereco="Rua B, 456",
        telefone="21988888888",
        email="maria@email.com"
    )
    conta2 = Conta(titular=cliente2, numero=54321, saldo=500.0, limite=300.0)

    print("\n--- Extrato inicial Conta 1 ---")
    print(conta1.extrato())
    print("\n--- Extrato inicial Conta 2 ---")
    print(conta2.extrato())

    # Teste de depósito válido
    print("\n--- Depósito válido em Conta 1 ---")
    sucesso, msg = conta1.deposita(500.0)
    print(f"Depósito: {msg}")
    print(conta1.extrato())

    # Teste de saque válido
    print("\n--- Saque válido em Conta 1 ---")
    sucesso, msg = conta1.saque(300.0)
    print(f"Saque: {msg}")
    print(conta1.extrato())

    # Teste de transferência entre contas
    print("\n--- Transferência de Conta 1 para Conta 2 ---")
    sucesso, msg = conta1.transferir(conta2, 700.0)
    print(f"Transferência: {msg}")
    print("\nExtrato Conta 1:")
    print(conta1.extrato())
    print("\nExtrato Conta 2:")
    print(conta2.extrato())

    # Teste de transferência com valor acima do saldo+limite
    print("\n--- Transferência acima do saldo+limite ---")
    sucesso, msg = conta1.transferir(conta2, 2000.0)
    print(f"Transferência: {msg}")

    # Teste de depósito e saque inválidos
    print("\n--- Depósito inválido em Conta 2 ---")
    sucesso, msg = conta2.deposita(-50.0)
    print(f"Depósito: {msg}")

    print("\n--- Saque inválido em Conta 2 ---")
    sucesso, msg = conta2.saque(0)
    print(f"Saque: {msg}")

    # Ajuste de saldo e limite diretamente
    print("\n--- Ajuste de saldo e limite em Conta 2 ---")
    try:
        conta2.saldo = 100.0
        print("Saldo ajustado para R$100.00 com sucesso.")
    except Exception as e:
        print(f"Erro ao ajustar saldo: {e}")
    try:
        conta2.limite = 800.0
        print("Limite ajustado para R$800.00 com sucesso.")
    except Exception as e:
        print(f"Erro ao ajustar limite: {e}")
    print(conta2.extrato())

    # Teste de ajuste de saldo e limite para valores negativos
    print("\n--- Ajuste de saldo negativo em Conta 2 ---")
    try:
        conta2.saldo = -10.0
    except Exception as e:
        print(f"Erro ao ajustar saldo: {e}")
    print("\n--- Ajuste de limite negativo em Conta 2 ---")
    try:
        conta2.limite = -100.0
    except Exception as e:
        print(f"Erro ao ajustar limite: {e}")

    print("\n--- Extrato final Conta 1 ---")
    print(conta1.extrato())
    print("\n--- Extrato final Conta 2 ---")
    print(conta2.extrato())

if __name__ == "__main__":
    main()
