# TABULAÇÕES E UNICODE EM STRINGS PYTHON
# --------------------------------------
# TABULAÇÃO (\t)
# A tabulação é uma sequência de escape (\t) que insere um "tab" (avanço horizontal) na string.
# Útil para alinhar colunas em textos ou tabelas simples.

print("Exemplo de tabulação:")
print("Nome\tIdade\tNota")
print("Ana\t23\t9.5")
print("Bruno\t30\t8.7")

# O número de espaços do tab depende do terminal/editor (geralmente 8, mas pode variar).
# Você pode ajustar o tamanho do tab usando o método expandtabs()
texto = "A\tB\tC"
print("Tabulação padrão:", texto)
print("Tabulação expandida:", texto.expandtabs(4))  # Cada tab vale 4 espaços

# Observe que tabulação não é igual a múltiplos espaços, mas pode ser convertida.

# UNICODE
# -------
# Unicode é um padrão universal para representar caracteres de praticamente todos os idiomas e símbolos.
# Strings em Python são Unicode por padrão (desde Python 3).

# Exemplos de caracteres Unicode:
print("Letra grega alfa: \u03B1")    # α
print("Símbolo de coração: \u2665")  # ♥
print("Emoji sorriso: \U0001F604")   # 😄

# Você pode usar códigos Unicode em qualquer string:
texto_unicode = "Matemática: \u03C0, \u221E, \u00B2"
print(texto_unicode)  # Matemática: π, ∞, ²

# Função ord() retorna o código Unicode de um caractere
print("Código Unicode de 'A':", ord('A'))  # 65
print("Código Unicode de 'ç':", ord('ç'))  # 231

# Função chr() retorna o caractere a partir do código Unicode
print("Caractere do código 9731:", chr(9731))  # ☃

# Você pode iterar por uma string e mostrar os códigos Unicode de cada caractere
palavra = "Olá!"
for letra in palavra:
    print(f"'{letra}' -> {ord(letra)}")

# DICA: Para descobrir o código Unicode de um símbolo, use ord() ou consulte https://unicode-table.com/pt/

# Exemplo de mistura de tabulação e Unicode:
print("Produto\tPreço")
print(f"Café\tR$ 5,00\t\u2615")  # ☕
print(f"Livro\tR$ 30,00\t\U0001F4D6")  # 📖
