usuario = str(input("Digite seu nome "))
qtd_caracteres = len(usuario)
print(qtd_caracteres)

if qtd_caracteres < 6:
    print('O nome deve ter no minimo 6 caracteres')
else:
    print("Voce foi castrado no sistema")