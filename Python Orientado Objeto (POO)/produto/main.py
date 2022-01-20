from product import Produto

p1 = Produto("CERVEJA", 'R$40')
print(p1.nome, p1.preco)
p1.desconto(20)
print(p1.nome, p1.preco)


p2 = Produto('CANECA', 'R$100')
print(p2.nome, p2.preco)
p2.desconto(10)
print(p2.nome, p2.preco)
