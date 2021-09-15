"""
operador ternario
"""

logged_user = True

if logged_user:
    msg = "Usuario logado"
else:
    msg = "Usuario precisa logar"

print(msg)

user_lagado = True

mensagem = "Usuario Logado" if user_lagado else "Usario precisa logar"

print(mensagem)


idade = 18

e_de_maior =  (idade >= 18)
txt = "Pode acessar" if e_de_maior else "Não pode acessar"
print(txt)

