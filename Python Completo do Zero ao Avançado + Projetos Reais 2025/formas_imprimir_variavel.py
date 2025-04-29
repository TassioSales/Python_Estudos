# VÁRIAS FORMAS DE IMPRIMIR VARIÁVEIS EM PYTHON
# ---------------------------------------------
# Suponha que temos as variáveis:
nome = "Ana"
idade = 30
nota = 9.75

# 1. Usando vírgula no print (forma simples)
print("Nome:", nome, "Idade:", idade, "Nota:", nota)

# 2. Usando concatenação (+) (precisa converter números para string)
print("Nome: " + nome + " | Idade: " + str(idade) + " | Nota: " + str(nota))

# 3. Usando f-string (moderno, recomendado - Python 3.6+)
print(f"Nome: {nome} | Idade: {idade} | Nota: {nota}")

# 4. Usando format()
print("Nome: {} | Idade: {} | Nota: {}".format(nome, idade, nota))

# 5. Usando format() com índices
print("Nome: {0} | Idade: {1} | Nota: {2}".format(nome, idade, nota))

# 6. Usando format() com nomes
print("Nome: {n} | Idade: {i} | Nota: {no}".format(n=nome, i=idade, no=nota))

# 7. Formatação antiga (% operador)
print("Nome: %s | Idade: %d | Nota: %.2f" % (nome, idade, nota))

# 8. F-string com formatação (casas decimais, alinhamento)
print(f"Nota formatada: {nota:.1f}")      # Uma casa decimal
print(f"Idade centralizada: {idade:^10}") # Centralizada em 10 espaços

# 9. F-string com expressões
print(f"Ano que vem, {nome} terá {idade + 1} anos.")

# 10. Multilinha com f-string
print(f"""
Resumo:
Nome: {nome}
Idade: {idade}
Nota: {nota}
""")

# 11. Usando join() para listas
valores = [nome, str(idade), str(nota)]
print(" | ".join(valores))
