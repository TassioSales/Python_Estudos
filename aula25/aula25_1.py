idade = input("Qual sua idade: ")

if not idade.isnumeric():
    print("Vocè deve digitar apenas numeros")

idade = int(idade)
e_de_maior = (idade >= 18)
txt = "Pode acessar" if e_de_maior else "Não pode acessar"
print(txt)
