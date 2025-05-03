# Estudo Interativo sobre Booleanos em Python

print("Bem-vindo ao Estudo Interativo de Booleanos!")
print("=" * 50)

while True:
    print("\nEscolha uma opção:")
    print("1. Booleanos básicos")
    print("2. Comparações")
    print("3. Operações lógicas")
    print("4. Condições")
    print("5. Booleanos com listas")
    print("6. Exemplo prático: Sistema de login")
    print("0. Sair")
    
    opcao = input("\nDigite o número da opção: ")
    
    if opcao == "0":
        print("\nObrigado por usar o programa!")
        break
        
    elif opcao == "1":
        print("\n1. Booleanos básicos")
        print("Booleanos são valores que podem ser True (verdadeiro) ou False (falso)")
        
        # Teste interativo
        valor = input("Digite True ou False: ")
        if valor.lower() == "true":
            print("Você digitou True!")
        elif valor.lower() == "false":
            print("Você digitou False!")
        else:
            print("Valor inválido!")
            
    elif opcao == "2":
        print("\n2. Comparações")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        print(f"\n{num1} > {num2}:", num1 > num2)
        print(f"{num1} < {num2}:", num1 < num2)
        print(f"{num1} == {num2}:", num1 == num2)
        print(f"{num1} != {num2}:", num1 != num2)
        
    elif opcao == "3":
        print("\n3. Operações lógicas")
        print("Teste as operações lógicas:")
        
        valor1 = input("Digite True ou False para o primeiro valor: ")
        valor2 = input("Digite True ou False para o segundo valor: ")
        
        valor1 = valor1.lower() == "true"
        valor2 = valor2.lower() == "true"
        
        print("\nResultados:")
        print(f"{valor1} AND {valor2} =", valor1 and valor2)
        print(f"{valor1} OR {valor2} =", valor1 or valor2)
        print(f"NOT {valor1} =", not valor1)
        
    elif opcao == "4":
        print("\n4. Uso em condições")
        idade = int(input("Digite sua idade: "))
        
        if idade >= 18:
            print("Você é maior de idade")
        else:
            print("Você é menor de idade")
            
        if idade >= 18 and idade <= 65:
            print("Você está na faixa etária de 18 a 65 anos")
        
    elif opcao == "5":
        print("\n5. Booleanos com listas")
        lista = []
        
        while True:
            item = input("Digite um item para adicionar à lista (ou 'sair' para terminar): ")
            if item.lower() == "sair":
                break
            lista.append(item)
        
        print("\nSua lista:", lista)
        busca = input("Digite um item para buscar na lista: ")
        
        if busca in lista:
            print(f"{busca} está na lista!")
        else:
            print(f"{busca} não está na lista!")
        
        if not lista:
            print("A lista está vazia!")
        else:
            print("A lista não está vazia!")
            
    elif opcao == "6":
        print("\n6. Exemplo prático: Sistema de login")
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        
        # Verificações
        usuario_valido = usuario == "admin"
        senha_valida = senha == "1234"
        
        # Login bem-sucedido
        login_sucesso = usuario_valido and senha_valida
        
        if login_sucesso:
            print("Login bem-sucedido!")
        else:
            print("Usuário ou senha incorretos!")
            
    else:
        print("Opção inválida! Tente novamente.")

print("\nFim do estudo sobre booleanos!")
