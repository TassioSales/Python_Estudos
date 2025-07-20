def cadastrar_produtos():
    """
    Permite cadastrar múltiplos produtos com nome e valor.
    Retorna uma lista de dicionários com os produtos cadastrados.
    """
    produtos = []
    while True:
        nome = input("Digite o nome do produto: ").strip()
        if not nome:
            print("Nome do produto não pode ser vazio.")
            continue
        while True:
            try:
                valor = float(input("Digite o valor do produto: R$ "))
                if valor <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido. Digite um número positivo.")
        produtos.append({"nome": nome, "valor": valor})
        continuar = input("Deseja cadastrar outro produto? (s/n): ").strip().lower()
        if continuar != 's':
            break
    return produtos

def exibir_produtos(produtos):
    """
    Exibe a lista de produtos cadastrados.
    """
    print("\nProdutos cadastrados:")
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. {produto['nome']} - R$ {produto['valor']:.2f}")

def main():
    produtos = cadastrar_produtos()
    exibir_produtos(produtos)

if __name__ == "__main__":
    main()
