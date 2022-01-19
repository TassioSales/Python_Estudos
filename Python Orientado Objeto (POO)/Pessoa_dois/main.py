from pessoa_dois import PessoaP

p1 = PessoaP("Luiz", 32)
p1.get_ano_nascimento()

p2 = PessoaP.por_ano_nascimento("Luiz", 1987)
print(p2)
print(p2.nome, p2.idade)
print(p2.idade)
p2.get_ano_nascimento()

