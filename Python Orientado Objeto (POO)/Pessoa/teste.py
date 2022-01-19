from pessoa import Pessoa

p1 = Pessoa("Luiz", 31)
p2 = Pessoa("João", 32)

p1.falar('POO')
p2.falar("Filmes")
p2.parar_falar()
p1.parar_falar()

p1.comer('churrasco')
p2.comer()

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

print(p1.ano_atual)
print(p2.ano_atual)