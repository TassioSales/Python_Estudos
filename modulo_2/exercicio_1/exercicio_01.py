"""
crie um função que exibe uma saudação com parametros saudação e nome
"""


def saudacao(msg="Ola", nome="Usuario"):
    print(f"{msg}, {nome}")


saudacao("Hello", "Tassio")
saudacao()
saudacao(nome="Rodrigo", msg="Como vai")
