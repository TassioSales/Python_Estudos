lista = [1, 2, 3, 4, 5]
var = "String"
lista = iter(lista)

print(hasattr(var, "__iter__"))
print(hasattr(lista, "__iter__"))

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

for v in lista:
    print(f"Numero {v}")
    
for c in var:
    print(c, end=",")