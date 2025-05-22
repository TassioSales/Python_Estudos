"""
Funções em Python - Conceitos Avançados

1. Funções como Objetos
   - Em Python, funções são objetos de primeira classe
   - Podem ser atribuídas a variáveis
   - Podem ser passadas como argumentos para outras funções
   - Podem ser retornadas por outras funções
"""

# Exemplo 1: Função como objeto
def saudacao():
    """Função simples de saudação"""
    return "Olá!"

# Atribuindo função a uma variável
minha_funcao = saudacao
print("\nExemplo 1 - Função como objeto:")
print(minha_funcao())  # Chama a função através da variável

"""
2. Funções Aninhadas (Nested Functions)
   - Funções podem ser definidas dentro de outras funções
   - A função interna tem acesso ao escopo da função externa
"""

def calculadora():
    """Função calculadora com funções aninhadas"""
    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    def multiplicar(a, b):
        return a * b
    
    def dividir(a, b):
        if b != 0:
            return a / b
        return "Divisão por zero não permitida"
    
    return somar, subtrair, multiplicar, dividir

# Usando as funções aninhadas
print("\nExemplo 2 - Funções Aninhadas:")
soma, sub, mult, div = calculadora()
print(f"Soma: {soma(5, 3)}")
print(f"Subtração: {sub(10, 5)}")
print(f"Multiplicação: {mult(4, 3)}")
print(f"Divisão: {div(10, 2)}")

"""
3. Funções Lambda (Funções Anônimas)
   - Funções simples que podem ser definidas em uma linha
   - Úteis para operações rápidas e temporárias
   - Sintaxe: lambda argumentos: expressão
"""

# Exemplo 3: Funções Lambda
print("\nExemplo 3 - Funções Lambda:")

# Função lambda para dobrar um número
dobrar = lambda x: x * 2
print(f"Dobro de 5: {dobrar(5)}")

# Função lambda para verificar se um número é par
par = lambda x: x % 2 == 0
print(f"5 é par? {par(5)}")
print(f"6 é par? {par(6)}")

"""
4. Funções com Decoradores
   - Decoradores são funções que modificam o comportamento de outras funções
   - Usam a sintaxe @decorador
"""

def decorador(funcao):
    """Decorador que adiciona '!' ao resultado da função"""
    def wrapper():
        return funcao() + "!"
    return wrapper

@decorador
def saudacao_decorada():
    return "Olá"

print("\nExemplo 4 - Funções com Decoradores:")
print(saudacao_decorada())  # Retorna "Olá!"

"""
5. Funções Geradoras (Generators)
   - Funções que retornam iteradores
   - Usam yield em vez de return
   - Úteis para trabalhar com sequências grandes
"""

def numeros_pares(maximo):
    """Gerador de números pares até um máximo"""
    numero = 0
    while numero <= maximo:
        yield numero
        numero += 2

print("\nExemplo 5 - Funções Geradoras:")
for numero in numeros_pares(10):
    print(numero, end=' ')

"""
6. Funções Recursivas
   - Funções que chamam a si mesmas
   - Úteis para resolver problemas que podem ser divididos em subproblemas
"""

def fatorial(n):
    """Calcula o fatorial de um número recursivamente"""
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

print("\n\nExemplo 6 - Funções Recursivas:")
print(f"Fatorial de 5: {fatorial(5)}")

"""
7. Funções com Argumentos Arbitrários
   - *args: aceita número variável de argumentos posicionais
   - **kwargs: aceita número variável de argumentos nomeados
"""

def exemplo_args_kwargs(*args, **kwargs):
    """Função que demonstra args e kwargs"""
    print("\nExemplo 7 - Args e Kwargs:")
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)
    
    # Exemplo de uso dos argumentos
    soma = sum(args)
    print(f"Soma dos argumentos posicionais: {soma}")
    
    # Exemplo de uso dos kwargs
    if 'nome' in kwargs:
        print(f"Olá, {kwargs['nome']}!")

# Chamando a função com diferentes tipos de argumentos
exemplo_args_kwargs(1, 2, 3, nome="Ana", idade=30, cidade="Rio")

"""
8. Funções com Parâmetros Opcionais e Valores Padrão
"""

def configurar_perfil(nome, idade=None, cidade="São Paulo", hobbies=[]):
    """Configura um perfil com informações opcionais"""
    perfil = {"nome": nome, "cidade": cidade}
    
    if idade:
        perfil["idade"] = idade
    
    if hobbies:
        perfil["hobbies"] = hobbies
    
    return perfil

print("\nExemplo 8 - Parâmetros Opcionais:")
perfil1 = configurar_perfil("João", idade=25)
perfil2 = configurar_perfil("Maria", cidade="Rio", hobbies=["leitura", "música"])
print("Perfil 1:", perfil1)
print("Perfil 2:", perfil2)

"""
9. Funções com Anotações de Tipo
   - Python 3.5+ suporta anotações de tipo
   - Ajuda na documentação e em ferramentas de análise
"""

def somar_numeros(a: int, b: int) -> int:
    """Função que soma dois números inteiros"""
    return a + b

print("\nExemplo 9 - Anotações de Tipo:")
resultado = somar_numeros(5, 3)
print(f"5 + 3 = {resultado}")

# Exemplo 1: Função simples sem parâmetros
def saudacao():
    """Esta função exibe uma mensagem de saudação"""
    print("Olá! Bem-vindo!")

"""
10. Funções com Docstrings Avançadas
   - Docstrings podem incluir parâmetros, retorno e exemplos
"""

def calcular_media(notas: list) -> float:
    """
    Calcula a média de uma lista de notas
    
    Args:
        notas (list): Lista de números representando notas
        
    Returns:
        float: Média das notas
        
    Raises:
        ValueError: Se a lista estiver vazia
        
    Examples:
        >>> calcular_media([7, 8, 9])
        8.0
        >>> calcular_media([10, 9, 8, 7])
        8.5
    """
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia")
    return sum(notas) / len(notas)

print("\nExemplo 10 - Docstrings Avançadas:")
try:
    media = calcular_media([7, 8, 9])
    print(f"Média das notas: {media}")
except ValueError as e:
    print(e)

"""
11. Funções com Arguments Unpacking
   - * para unpacking de listas/tuplas
   - ** para unpacking de dicionários
"""

def mostrar_dados(nome, idade, cidade):
    """Mostra dados do usuário"""
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

print("\nExemplo 11 - Arguments Unpacking:")

# Unpacking de lista
dados_lista = ["Ana", 30, "São Paulo"]
mostrar_dados(*dados_lista)

# Unpacking de dicionário
dados_dict = {"nome": "João", "idade": 25, "cidade": "Rio"}
mostrar_dados(**dados_dict)

"""
12. Funções com Closures
   - Closures são funções que "lembram" valores do escopo externo
   - Úteis para criar funções com estado
"""

def criar_saudacao(saudacao):
    """Função que cria uma saudação personalizada"""
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

print("\nExemplo 12 - Closures:")
saudar_bom_dia = criar_saudacao("Bom dia")
saudar_boa_noite = criar_saudacao("Boa noite")

print(saudar_bom_dia("Maria"))
print(saudar_boa_noite("João"))

"""
13. Funções com Decoradores com Parâmetros
"""

def repetir(n):
    """Decorador que repete a execução de uma função n vezes"""
    def decorador(funcao):
        def wrapper():
            for _ in range(n):
                funcao()
        return wrapper
    return decorador

@repetir(3)
def dizer_ola():
    print("Olá!")

print("\nExemplo 13 - Decoradores com Parâmetros:")
dizer_ola()

"""
14. Funções com Argumentos Padrão Mutáveis
   - Cuidado com argumentos padrão mutáveis
   - Eles são criados apenas uma vez no momento da definição
"""

def adicionar_item(item, lista=[]):
    """Adiciona um item a uma lista (exemplo problemático)"""
    lista.append(item)
    return lista

print("\nExemplo 14 - Argumentos Mutáveis:")
print(adicionar_item("maçã"))  # ['maçã']
print(adicionar_item("banana"))  # ['maçã', 'banana']

# Solução correta
print("\nSolução correta:")
def adicionar_item_correto(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

print(adicionar_item_correto("laranja"))  # ['laranja']
print(adicionar_item_correto("uva"))  # ['uva']

"""
15. Funções com Argumentos Decorados
"""

def decorar_argumento(funcao):
    """Decorador que decora o argumento da função"""
    def wrapper(*args):
        decorado = [f"*{arg}*" for arg in args]
        return funcao(*decorado)
    return wrapper

@decorar_argumento
def mostrar_itens(*itens):
    """Mostra itens com decoração"""
    for item in itens:
        print(item)

print("\nExemplo 15 - Decoradores de Argumentos:")
mostrar_itens("livro", "caneta", "caderno")

"""
Conceitos importantes sobre funções:
1. Docstrings: Documentação completa da função
2. Escopo: Variáveis locais e globais
3. Tipos de Parâmetros:
   - Obrigatórios
   - Opcionais com valores padrão
   - Args (argumentos variáveis)
   - Kwargs (argumentos nomeados)
4. Return: Pode retornar múltiplos valores usando tuplas
5. Decoradores: Modificam o comportamento de funções
6. Closures: Funções que "lembram" valores do escopo externo
7. Generators: Funções que criam iteradores
8. Recursividade: Funções que chamam a si mesmas
9. Anotações de Tipo: Para melhor documentação e análise
10. Unpacking: Desempacotamento de argumentos
"""

# Exemplo de retorno múltiplo usando tuplas
def calcular_estatisticas(numeros):
    """Calcula média, mínima e máxima de uma lista de números"""
    media = sum(numeros) / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return media, minimo, maximo

print("\nExemplo de Retorno Múltiplo:")
media, minimo, maximo = calcular_estatisticas([1, 2, 3, 4, 5])
print(f"Média: {media}, Mínimo: {minimo}, Máximo: {maximo}")

# Exemplo 2: Função com parâmetros
def saudacao_personalizada(nome):
    """Esta função exibe uma saudação personalizada"""
    print(f"Olá, {nome}! Seja bem-vindo!")

# Exemplo 3: Função com retorno
def calcular_area_retangulo(largura, altura):
    """Calcula a área de um retângulo"""
    return largura * altura

# Exemplo 4: Função com parâmetros padrão
def calcular_volume_caixa(largura=2, altura=3, profundidade=4):
    """Calcula o volume de uma caixa com valores padrão"""
    return largura * altura * profundidade

# Exemplo 5: Função com múltiplos parâmetros
def calcular_media(*notas):
    """Calcula a média de um número variável de notas"""
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Exemplo 6: Função com parâmetros nomeados
def configurar_perfil(nome, idade=None, cidade="São Paulo"):
    """Configura um perfil com informações opcionais"""
    perfil = {"nome": nome}
    if idade:
        perfil["idade"] = idade
    perfil["cidade"] = cidade
    return perfil

# Exemplo de uso das funções
print("\nExemplo 1 - Função simples:")
saudacao()

print("\nExemplo 2 - Função com parâmetro:")
saudacao_personalizada("Maria")

print("\nExemplo 3 - Função com retorno:")
area = calcular_area_retangulo(5, 3)
print(f"Área do retângulo: {area}")

print("\nExemplo 4 - Função com parâmetros padrão:")
volume = calcular_volume_caixa()
print(f"Volume da caixa (padrão): {volume}")
volume = calcular_volume_caixa(2, 4, 6)
print(f"Volume da caixa (personalizado): {volume}")

print("\nExemplo 5 - Função com múltiplos parâmetros:")
media = calcular_media(7, 8, 9, 10)
print(f"Média das notas: {media}")

print("\nExemplo 6 - Função com parâmetros nomeados:")
perfil = configurar_perfil("João", idade=25, cidade="Rio de Janeiro")
print("Perfil:", perfil)

"""
Conceitos importantes sobre funções:
1. Docstrings: As strings entre """ """ são documentação da função
2. Escopo: As variáveis dentro da função só existem dentro dela
3. Parâmetros:
   - Obrigatórios: devem ser passados sempre
   - Opcionais: têm valores padrão
   - *args: aceita número variável de argumentos posicionais
   - **kwargs: aceita número variável de argumentos nomeados
4. Return: Retorna um valor da função
   - Se não houver return, a função retorna None
"""

# Exemplo de função com *args e **kwargs
def exemplo_args_kwargs(*args, **kwargs):
    """Exemplo de função que aceita argumentos posicionais e nomeados"""
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)

print("\nExemplo de *args e **kwargs:")
exemplo_args_kwargs(1, 2, 3, nome="Ana", idade=30)
