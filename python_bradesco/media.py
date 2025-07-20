#cria uma funcao para pegar as notas de 4 semestres
def ler_notas():
    notas = []
    for i in range(4):
        while True:
            try:
                nota_str = input(f"Digite a nota do {i+1}º semestre: ")
                nota = float(nota_str.replace(",", "."))
                notas.append(nota)
                break
            except ValueError:
                print("Nota inválida. Por favor, digite um número válido.")
    return notas

#calcula a media das notas
def calcular_media(notas):
    """Calcula a média das notas de um aluno."""
    try:
        if not notas:
            raise ValueError("A lista de notas está vazia.")
        media = sum(notas) / len(notas)
        return media
    except ValueError as e:
        print(f"Erro: {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

def main():
    try:
        notas = ler_notas()
        media = calcular_media(notas)
        if media is not None:
            print(f"A média das notas é: {media:.2f}")
            if 5 <= media < 7:
                print("Aprovado")
            elif 7 <= media < 9:
                print("Parabens voce passou com sucesso")
            elif 9 <= media <= 10:
                print("Parabens vc passou com excelencia")
            else:
                print("Reprovado")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()