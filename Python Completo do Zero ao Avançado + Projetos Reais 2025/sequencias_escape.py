# SEQUÊNCIAS DE ESCAPE EM STRINGS PYTHON
# --------------------------------------
# Sequências de escape são usadas para inserir caracteres especiais em strings.
# Elas começam com uma barra invertida (\) seguida de um caractere especial.

# Exemplos comuns:

# \n - Quebra de linha (newline)
print("Primeira linha\nSegunda linha")

# \t - Tabulação (tab)
print("Coluna 1\tColuna 2\tColuna 3")

# \\ - Barra invertida
print("Caminho: C:\\Users\\Ana")

# \' e \" - Aspas simples e duplas dentro de strings
print('Ela disse: \"Oi!\"')
print("It\'s a beautiful day!")

# \r - Retorno de carro (carriage return, raramente usado)
print("ABC\r123")  # O '123' sobrescreve o 'ABC' em alguns terminais

# \b - Backspace (apaga o caractere anterior, efeito depende do terminal)
print("ABC\bD")  # Pode mostrar 'ABD' ou 'AB\bD' dependendo do terminal

# \a - Sinal sonoro (bell, pode emitir um som)
print("Alerta!\a")

# \u e \U - Unicode (caracteres especiais)
print("Letra grega: \u03B1")  # α
print("Emoji: \U0001F600")    # 😀

# Exemplos práticos:
texto = "Linha 1\n\t* Item 1\n\t* Item 2\nLinha 2"
print(texto)

# DICA: Para mostrar a barra invertida sem ativar escape, use r'string' (raw string):
print(r"C:\Users\Ana")  # Mostra exatamente como está, sem aplicar escapes

# --------------------------------------
# MAIS MÉTODOS ÚTEIS DE STRING

# .strip(), .lstrip(), .rstrip() - Remove espaços (ou caracteres) das pontas
texto = "   exemplo   "
print(texto.strip())    # 'exemplo'
print(texto.lstrip())   # 'exemplo   '
print(texto.rstrip())   # '   exemplo'

# .center(), .ljust(), .rjust() - Centraliza ou alinha a string, preenchendo com caracteres
print("abc".center(10, "-"))  # '---abc----'
print("abc".ljust(10, "."))   # 'abc.......'
print("abc".rjust(10, "."))   # '.......abc'

# .zfill() - Preenche com zeros à esquerda
print("42".zfill(5))  # '00042'

# .isnumeric(), .isdecimal(), .isdigit() - Testa se a string representa números
print("123".isnumeric())   # True
print("½".isnumeric())     # True (caractere especial)
print("123".isdecimal())   # True
print("123".isdigit())     # True

# .isupper(), .islower(), .istitle() - Testa se está tudo maiúsculo, minúsculo ou título
print("ABC".isupper())     # True
print("abc".islower())     # True
print("Python Rocks".istitle())  # True

# .swapcase() - Inverte maiúsculas e minúsculas
print("PyThOn".swapcase())  # 'pYtHoN'

# .startswith(), .endswith() - Testa se começa ou termina com algo
print("banana".startswith("ba"))  # True
print("banana".endswith("na"))    # True

# .partition(), .rpartition() - Divide a string em 3 partes
print("email@gmail.com".partition("@"))  # ('email', '@', 'gmail.com')
print("a-b-c-d".rpartition("-"))         # ('a-b-c', '-', 'd')
