def calcular_potencias():
    # Solicita a base da potência ao usuário
    base = int(input("Digite a base da potência: "))
    # Solicita o número final ao usuário
    numero_final = int(input("Digite até qual número deseja calcular: "))
    
    # Inicia a contagem a partir da base
    numero = base
    while numero <= numero_final:
        print(f"{base} ** {numero} = {base ** numero}")
        numero += 1

# Executa a função
if __name__ == "__main__":
    calcular_potencias()
