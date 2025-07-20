class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente
from Conta import Conta
import random

c1 = Cliente("Maria", "12345678901", "20/01/1990", "F", "Casada", "Engenheira", "Brasileira", "São Paulo", "Rua das Flores, 123", "11 98765-4321", "william.henry.harrison@example-pet-store.com")

print(c1)
print(f'Nome: {c1.nome} e CPF: {c1.cpf}')

conta = Conta(c1.nome, random.randint(1000, 9999), 5000, 2500)

print(f"Titular: {conta.titular} - Número: {conta.numero} - Saldo: {conta.saldo} - Limite: {conta.limite}")