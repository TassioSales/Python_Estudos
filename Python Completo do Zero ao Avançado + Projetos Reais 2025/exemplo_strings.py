# EXPLICANDO STRINGS EM PYTHON
# -------------------------------------
# String é um tipo de dado usado para representar texto em Python.
# Uma string é uma sequência de caracteres, ou seja, letras, números, símbolos, espaços, etc.

# Como criar uma string:
texto1 = "Olá, mundo!"  # Usando aspas duplas
texto2 = 'Python é divertido'  # Usando aspas simples
texto3 = """Esta é\numa string\nde múltiplas linhas"""  # Aspas triplas para múltiplas linhas

print(texto1)
print(texto2)
print(texto3)

# Strings podem conter qualquer caractere:
exemplo = "1234!@# abc"
print(exemplo)

# -------------------------------------
# ÍNDICES (INDEX) EM STRINGS
# Cada caractere de uma string tem uma posição, chamada de índice.
# O índice começa do 0 para a esquerda e pode ser negativo para contar da direita.
# Exemplo visual:
# texto = "Python"
# Índices:  0  1  2  3  4  5
#           P  y  t  h  o  n
# Índices: -6 -5 -4 -3 -2 -1

texto_exemplo = "Python"
print("Texto de exemplo:", texto_exemplo)
print("Caractere na posição 0:", texto_exemplo[0])   # 'P'
print("Caractere na posição 3:", texto_exemplo[3])   # 'h'
print("Último caractere:", texto_exemplo[-1])        # 'n'
print("Penúltimo caractere:", texto_exemplo[-2])    # 'o'

# Se tentar acessar um índice que não existe, dá erro:
# print(texto_exemplo[10])  # IndexError

# Também é possível usar índices em laços:
for i in range(len(texto_exemplo)):
    print(f"Índice {i}: {texto_exemplo[i]}")

# Exemplos práticos de acesso a letras específicas:
palavra = "abacaxi"
print("Letra na posição 2 de 'abacaxi':", palavra[2])  # 'a' (lembre-se: começa do 0)
print("Letra na posição 0 de 'abacaxi':", palavra[0])  # 'a'
print("Letra na posição 5 de 'abacaxi':", palavra[5])  # 'x'
print("Última letra de 'abacaxi':", palavra[-1])       # 'i'

# Você pode usar isso em qualquer string:
fruta = "morango"
print("Terceira letra de 'morango':", fruta[2])        # 'r'

# Também pode pedir para o usuário digitar uma palavra e mostrar uma letra específica:
# entrada = input("Digite uma palavra: ")
# print("A segunda letra é:", entrada[1])

# -------------------------------------
# TAMANHO DA STRING
# Para saber quantos caracteres tem uma string, use len()
texto_tam = "Python"
print("Tamanho da string 'Python':", len(texto_tam))  # 6
print("Tamanho de 'Olá, mundo!':", len(texto1))       # 12

# -------------------------------------
# FATIAMENTO (SLICE) DE STRINGS
# Podemos pegar partes de uma string usando colchetes e dois pontos: string[inicio:fim]
# O início é incluso, o fim não é incluso.
frase = "Aprendendo Python"
print("Fatiamento 0:5:", frase[0:5])    # 'Apren' (do índice 0 ao 4)
print("Fatiamento 6:14:", frase[6:14])  # 'ndo Pyth'
print("Fatiamento até o índice 9:", frase[:9])  # 'Aprenden'
print("Fatiamento do índice 11 até o final:", frase[11:])  # 'Python'
print("Fatiamento com passo 2:", frase[0:10:2])  # 'Aredn' (de 2 em 2)
print("String invertida:", frase[::-1])  # Inverte a string

# -------------------------------------
# Como acessar caracteres individuais (indexação):
# Lembre-se: o primeiro caractere está na posição 0
primeira_letra = texto1[0]  # 'O'
ultima_letra = texto1[-1]   # '!'
print("Primeira letra:", primeira_letra)
print("Última letra:", ultima_letra)

# Como pegar partes de uma string (fatiamento/slice):
sub_texto = texto1[0:5]  # Vai do índice 0 até o 4 (não inclui o 5)
print("Fatiamento:", sub_texto)

# CONCATENAÇÃO DE STRINGS
# Juntar textos é muito comum em programação:
nome = "Maria"
saudacao = "Olá, " + nome + "!"  # Usando o operador +
print(saudacao)

# Usando f-string (forma moderna e recomendada):
idade = 25
mensagem = f"{nome} tem {idade} anos."
print(mensagem)

# Usando o método join para juntar vários textos:
palavras = ["Python", "é", "legal"]
frase = " ".join(palavras)
print(frase)

# Repetição de strings:
linha = "-" * 20
print(linha)

# MÉTODOS ÚTEIS DE STRING
print(nome.upper())      # 'MARIA' (tudo maiúsculo)
print(nome.lower())      # 'maria' (tudo minúsculo)
print(nome.replace("a", "@"))  # 'M@ri@' (troca 'a' por '@')

# Verificando se um texto está dentro de outro:
print("Maria" in saudacao)  # True
print("João" in saudacao)   # False

# Removendo espaços extras:
espacos = "  texto com espaços   "
print(espacos.strip())  # 'texto com espaços'

# MAIS EXEMPLOS PRÁTICOS:
# 1. Contar quantas vezes um caractere aparece:
frase2 = "banana"
print(frase2.count("a"))  # 3

# 2. Encontrar a posição de um caractere:
print(frase2.find("n"))  # 2 (primeira ocorrência)

# 3. Substituir partes do texto:
email = "meuemail@gmail.com"
print(email.replace("gmail", "hotmail"))  # 'meuemail@hotmail.com'

# 4. Quebrar uma string em partes (split):
data = "28/04/2025"
partes = data.split("/")
print(partes)  # ['28', '04', '2025']

# 5. Juntar listas em uma string:
reuniao = ", ".join(["Ana", "Bruno", "Carlos"])
print("Participantes:", reuniao)

# 6. Formatação antiga (não recomendada, mas comum em códigos antigos):
nota = 9.5
print("%s tirou nota %.1f" % (nome, nota))

# 7. Verificar se começa ou termina com algo:
print(email.startswith("meu"))  # True
print(email.endswith(".com"))   # True

# 8. Deixar a primeira letra maiúscula:
print(nome.capitalize())  # 'Maria'

# 9. Remover tudo de uma string (string vazia):
vazio = ""
print("Está vazia?", len(vazio) == 0)

# 10. Exemplo de uso prático: criar uma mensagem personalizada
usuario = "Lucas"
produto = "livro"
mensagem_personalizada = f"Olá, {usuario}! Obrigado por comprar o {produto}."
print(mensagem_personalizada)

# DICA: Sempre que quiser saber o que dá pra fazer com uma string, use help(str) ou dir(str) no Python!
