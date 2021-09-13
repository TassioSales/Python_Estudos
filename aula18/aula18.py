frase =  "O rato roeu a ropa do rei de roma"
tamanho_frase = len("frase")

contador = 0
nova_string = ""

# while contador < 10:
#     print(contador)
#     contador += 1


while contador < len(frase):
    print(frase[contador].upper(), contador)
    nova_string += frase[contador].upper()
    contador += 1

print(nova_string)