texto = "Python"

c = 0

while c < len("texto"):
    print(texto[c])
    c += 1

print()

for letra in texto:
    print(letra)

print()

for c, letra in enumerate(texto):
    print(letra, c)



