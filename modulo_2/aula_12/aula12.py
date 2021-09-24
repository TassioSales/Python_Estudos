nome = "Tassio Sales"
iterador = iter(nome)
gerador = (letra for letra in nome)

for letra in nome:
    print(letra, end=",")

print("\n")
    
for letra in gerador:
    print(letra)

print("\n")
print("#" * 80)
print("\n")

for letra in nome:
    print(letra, end=",")

print("\n")

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except:
    pass

print("CADE OS VALORES")
for valor in iterador:
    print(valor)