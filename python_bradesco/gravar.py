def criar_arquivo():
    """Pede um nome de arquivo ao usuário e o cria."""
    nome_arquivo = input("Digite o nome do arquivo a ser criado: ")
    try:
        # O modo 'w' cria um novo arquivo para escrita.
        # Se o arquivo já existir, seu conteúdo será apagado.
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
        return nome_arquivo
    except IOError as e:
        print(f"Ocorreu um erro de E/S (Entrada/Saída) ao criar o arquivo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def escrever_no_arquivo(nome_arquivo, texto):
    """Escreve uma linha de texto no final do arquivo especificado."""
    try:
        # Usamos o modo 'a' (append) para adicionar conteúdo ao final do arquivo.
        # Se você quisesse substituir todo o conteúdo, usaria o modo 'w' (write).
        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(texto + "\n") # Adiciona uma nova linha para melhor formatação
            print(f"Texto adicionado com sucesso ao arquivo '{nome_arquivo}'!")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao escrever no arquivo: {e}")


def main():
    """Função principal para executar o script."""
    nome_do_arquivo = criar_arquivo()
    if nome_do_arquivo:
        texto_para_escrever = input("Digite o texto que deseja gravar no arquivo: ")
        escrever_no_arquivo(nome_do_arquivo, texto_para_escrever)

# Executa a função main quando o script é iniciado
if __name__ == "__main__":
    main()

