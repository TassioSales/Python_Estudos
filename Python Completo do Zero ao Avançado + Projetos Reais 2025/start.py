import sys
def HelloWord():
    # Função que imprime Hello Word
    # e o nome do usuário
    texto = "Hello World!"
    nome = "Tassio"
    TextoFinal = print(f"{texto} {nome}")
    return TextoFinal

def TiposDeVariaveis():
    string = "As variaveis são do tipo string e são utilizadas para armazenar textos."
    inteiros = "As variaveis são do tipo inteiro e são utilizadas para armazenar números inteiros."
    decimais = "As variaveis são do tipo decimal e são utilizadas para armazenar números decimais."
    booleanos = "As variaveis são do tipo booleano e são utilizadas para armazenar valores lógicos (True ou False)."
    none = "As variaveis são do tipo none e são utilizadas para armazenar valores nulos."
    ExString = "Exemplo de string: 'Olá, mundo!'"
    ExInteiro = "Exemplo de inteiro: 10"
    ExDecimal = "Exemplo de decimal: 3.14"
    ExBooleano = "Exemplo de booleano: True"
    Exnone = "Exemplo de none: None"
    sys.stdout.buffer.write(f"String: {string} Exemplo: {ExString}\n".encode('utf-8'))
    sys.stdout.buffer.write(f"Inteiro: {inteiros} Exemplo: {ExInteiro}\n".encode('utf-8'))
    sys.stdout.buffer.write(f"Decimal: {decimais} Exemplo: {ExDecimal}\n".encode('utf-8'))
    sys.stdout.buffer.write(f"Booleano: {booleanos} Exemplo: {ExBooleano}\n".encode('utf-8'))
    sys.stdout.buffer.write(f"None: {none} Exemplo: {Exnone}\n".encode('utf-8'))
    
def MostrandoOsTiposDeVariaveis():
    texto = "Hello World!"
    inteiro = 10
    decimal = 3.14
    booleano = True
    none = None
    
    sys.stdout.buffer.write(f"Tipo de texto: {type(texto)}\n".encode('utf-8'))
    sys.stdout.buffer.write(f"Tipo de inteiro: {type(inteiro)}\n".encode('utf-8'))
    sys.stdout.buffer.write(f"Tipo de decimal: {type(decimal)}\n".encode('utf-8'))
    sys.stdout.buffer.write(f"Tipo de booleano: {type(booleano)}\n".encode('utf-8'))
    sys.stdout.buffer.write(f"Tipo de none: {type(none)}\n".encode('utf-8'))
    


if __name__ == "__main__":
    HelloWord()
    print("-"*120)
    TiposDeVariaveis()
    print("-"*120)
    MostrandoOsTiposDeVariaveis()