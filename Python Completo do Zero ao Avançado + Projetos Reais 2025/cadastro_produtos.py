
def input_nome_produto(produtos_existentes=None):
    """
    Solicita e valida o nome do produto. Garante que não seja vazio e, se fornecido, que seja único.
    """
    while True:
        nome = input("Digite o nome do produto: ").strip()
        if not nome:
            print("Nome do produto não pode ser vazio.")
            continue
        if produtos_existentes is not None and nome in produtos_existentes:
            print("Produto já cadastrado. Digite um nome diferente.")
            continue
        return nome

def input_valor_produto():
    """
    Solicita e valida o valor do produto. Garante que seja um número positivo.
    """
    while True:
        try:
            valor = float(input("Digite o valor do produto: R$ "))
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            print("Valor inválido. Digite um número positivo.")

def cadastrar_produtos():
    """
    Permite cadastrar múltiplos produtos com nome e valor.
    Retorna uma lista de dicionários com os produtos cadastrados.
    """
    produtos = []
    nomes_cadastrados = set()
    print("\n=== Cadastro de Produtos ===")
    try:
        while True:
            nome = input_nome_produto(nomes_cadastrados)
            valor = input_valor_produto()
            produtos.append({"nome": nome, "valor": valor})
            nomes_cadastrados.add(nome)
            continuar = input("Deseja cadastrar outro produto? (s/n): ").strip().lower()
            if continuar != 's':
                break
    except KeyboardInterrupt:
        print("\nCadastro interrompido pelo usuário.")
    return produtos

def exibir_produtos(produtos):
    """
    Exibe a lista de produtos cadastrados de forma formatada e mostra o total.
    """
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return
    print("\n=== Produtos cadastrados ===")
    print(f"{'#':<3} {'Produto':<20} {'Valor (R$)':>12}")
    print("-" * 38)
    total = 0
    for i, produto in enumerate(produtos, 1):
        print(f"{i:<3} {produto['nome']:<20} {produto['valor']:>12.2f}")
        total += produto['valor']
    print("-" * 38)
    print(f"{'Total':<23} {total:>12.2f}")

def main():
    produtos = cadastrar_produtos()
    exibir_produtos(produtos)

if __name__ == "__main__":
    main()
