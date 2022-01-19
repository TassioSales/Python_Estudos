from pessoa import Pessoa

p1 = Pessoa("Tassio", 31)

print(p1.mostra())
print(p1.comer(alimento="Maça"))
p1.parar_comer()
p1.comer(alimento="Uva")
p1.parar_comer()
p1.falar("POO")
p1.comer(alimento="Sanduiche")
p1.parar_falar()
p1.falar('Assunto')
