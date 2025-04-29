# MÉTODOS E FUNÇÕES COMUNS PARA STRINGS EM PYTHON
# ------------------------------------------------
# Existem vários métodos e funções úteis para trabalhar com strings em Python.
# Métodos são funções que "pertencem" ao objeto string e são usados assim: string.metodo()
# Funções podem ser usadas diretamente, como len(string)

texto = "  Python é muito poderoso!  "

# 1. len() - Retorna o tamanho (número de caracteres) da string
print("Tamanho:", len(texto))

# 2. strip() - Remove espaços em branco do início e do fim
t = texto.strip()
print("Sem espaços nas pontas:", t)

# 3. lower() e upper() - Converte para minúsculas ou maiúsculas
print("Minúsculas:", texto.lower())
print("Maiúsculas:", texto.upper())

# 4. capitalize() - Primeira letra maiúscula, resto minúsculo
print("Capitalizada:", texto.capitalize())

# 5. title() - Primeira letra de cada palavra maiúscula
print("Título:", texto.title())

# 6. replace() - Troca partes da string
print("Troca 'Python' por 'Java':", texto.replace("Python", "Java"))

# 7. split() - Quebra a string em uma lista, usando espaço como padrão
palavras = texto.split()
print("Lista de palavras:", palavras)

# 8. join() - Junta elementos de uma lista em uma string
lista = ["a", "b", "c"]
junto = "-".join(lista)
print("Juntando lista:", junto)

# 9. find() - Retorna o índice da primeira ocorrência do texto procurado
print("Posição de 'muito':", texto.find("muito"))

# 10. count() - Conta quantas vezes aparece um caractere ou substring
print("Quantidade de 'o':", texto.count("o"))

# 11. startswith() e endswith() - Verifica se começa ou termina com determinado texto
print("Começa com '  Py':", texto.startswith("  Py"))
print("Termina com '!  ':", texto.endswith("!  "))

# 12. isalpha(), isdigit(), isalnum(), isspace() - Testa se a string é só letras, números, alfanumérica ou só espaços
print("Só letras:", "abcde".isalpha())
print("Só números:", "12345".isdigit())
print("Alfanumérico:", "abc123".isalnum())
print("Só espaço:", "   ".isspace())

# 13. zfill() - Preenche com zeros à esquerda
codigo = "42"
print("Código com zeros:", codigo.zfill(5))  # '00042'

# 14. center(), ljust(), rjust() - Centraliza, alinha à esquerda ou à direita
print("Centralizado:", texto.center(40, '-'))
print("À esquerda:", texto.ljust(30, '.'))
print("À direita:", texto.rjust(30, '.'))

# 15. enumerate() - Útil para percorrer string com índice
for i, letra in enumerate("exemplo"):
    print(f"Índice {i}: {letra}")

# --- MÉTODOS ADICIONAIS ---
texto2 = "Python é incrível!"

# swapcase() - Inverte maiúsculas e minúsculas
print(texto2.swapcase())  # 'pYTHON É INCRÍVEL!'

# casefold() - Versão mais agressiva do lower(), útil para comparações
print("straße".casefold() == "STRASSE".casefold())  # True

# partition() - Divide a string em 3 partes: antes, separador, depois
print(texto2.partition("é"))  # ('Python ', 'é', ' incrível!')

# rpartition() - Igual ao partition, mas procura o separador da direita
print(texto2.rpartition("i"))  # ('Python é incr', 'i', 'vel!')

# rsplit() - Igual ao split, mas começa da direita
print("a,b,c,d".rsplit(",", 1))  # ['a,b,c', 'd']

# rfind() - Encontra a última ocorrência de um valor
print(texto2.rfind("i"))  # 13

# rindex() - Igual ao rfind, mas dá erro se não encontrar
print(texto2.rindex("i"))  # 13

# expandtabs() - Substitui tabulações por espaços
print("a\tb\tc".expandtabs(4))  # 'a   b   c'

# format() - Formata strings (útil para versões antigas do Python)
print("Olá, {}!".format("João"))

# islower() e isupper() - Verifica se está tudo minúsculo ou maiúsculo
print("abc".islower())  # True
print("ABC".isupper())  # True

# isnumeric(), isdecimal() - Verifica se a string representa números
print("123".isnumeric())  # True
print("½".isnumeric())    # True

# isidentifier() - Verifica se pode ser um nome de variável
print("variavel1".isidentifier())  # True
print("1variavel".isidentifier())  # False

# removeprefix() e removesuffix() (Python 3.9+)
print("unittest".removeprefix("unit"))  # 'test'
print("testcase".removesuffix("case"))  # 'test'

# DICA: Para ver todos os métodos disponíveis, use dir(str) ou help(str)
