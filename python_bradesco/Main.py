from Cliente import Cliente
from Conta import Conta
import random

def main():
    """
    Exemplo simples de uso das classes Cliente e Conta.
    """
    # Criação de um cliente
    cliente = Cliente(
        nome="Maria",
        cpf="12345678901",
        data_nascimento="20/01/1990",
        sexo="F",
        estado_civil="Casada",
        profissao="Engenheira",
        nacionalidade="Brasileira",
        naturalidade="São Paulo",
        endereco="Rua das Flores, 123",
        telefone="11987654321",
        email="maria@example.com"
    )

    print("\n--- Dados do Cliente ---")
    print(cliente)
    print(f'Nome: {cliente.nome} | CPF: {cliente.cpf}')

    # Criação de uma conta para o cliente
    conta = Conta(
        titular=cliente,  # Agora o titular é o objeto Cliente
        numero=random.randint(1000, 9999),
        saldo=5000.0,
        limite=2500.0
    )

    print("\n--- Dados da Conta ---")
    print(conta)
    print(conta.extrato())

    # Realizando um depósito
    print("\n--- Depósito de R$1000.00 ---")
    sucesso, msg = conta.deposita(1000.0)
    print(msg)
    print(conta.extrato())

    # Realizando um saque
    print("\n--- Saque de R$2000.00 ---")
    sucesso, msg = conta.saque(2000.0)
    print(msg)
    print(conta.extrato())

    # Tentando sacar valor acima do saldo+limite
    print("\n--- Saque acima do saldo+limite ---")
    sucesso, msg = conta.saque(10000.0)
    print(msg)
    print(conta.extrato())

if __name__ == "__main__":
    main()
