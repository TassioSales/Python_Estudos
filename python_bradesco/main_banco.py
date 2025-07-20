from Conta import Conta

# Criação de uma conta
conta = Conta(titular="João Silva", numero=12345, saldo=1000.0, limite=500.0)

print("--- Extrato inicial ---")
print(conta.extrato())
print()

# Teste de depósito válido
deposito_sucesso, msg = conta.deposita(500.0)
print(f"Depósito: {msg}")
print(conta.extrato())
print()

# Teste de depósito inválido
deposito_sucesso, msg = conta.deposita(-100.0)
print(f"Depósito: {msg}")
print()

# Teste de saque válido
saque_sucesso, msg = conta.saque(300.0)
print(f"Saque: {msg}")
print(conta.extrato())
print()

# Teste de saque acima do saldo+limite
saque_sucesso, msg = conta.saque(2000.0)
print(f"Saque: {msg}")
print()

# Ajuste de saldo diretamente (usando setter)
try:
    conta.saldo = 200.0
    print("Saldo ajustado para R$200.00 com sucesso.")
except Exception as e:
    print(f"Erro ao ajustar saldo: {e}")
print(conta.extrato())
print()

# Ajuste de limite diretamente (usando setter)
try:
    conta.limite = 1000.0
    print("Limite ajustado para R$1000.00 com sucesso.")
except Exception as e:
    print(f"Erro ao ajustar limite: {e}")
print(conta.extrato())
print()

# Teste de saque usando novo limite
saque_sucesso, msg = conta.saque(1100.0)
print(f"Saque: {msg}")
print(conta.extrato())
