secreta = "perfume"
digitado = []

while True:
    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("Digite somente uma letra")
        continue
        
    digitado.append(letra)

    if letra in secreta:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print(f"A letra {letra} não existe na palavra secreta")
        digitado.pop()

    secreto_temporario = ""
    for letra_secreta in secreta:
        if letra_secreta in digitado:
            secreto_temporario += letra
        else:
            secreto_temporario  += "*"
    print(secreto_temporario)

    if secreto_temporario == secreta:
        print("Voce ganhou")
    else:
        print("Voce perdeu")
        