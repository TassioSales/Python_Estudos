"""
laço de repetição while
"""

while True:
    nome = str(input("Qual seu nome: "))
    print(f"Prazer em te conhecer {nome}")
    break

x = 0
while x < 11:
    if x % 2 == 1:
        x += 1
        continue
    print(x, end=", ")
    x += 1

print("\n")

y = 0
while y < 10:
    if y == 8:
        break
    print(y, end=", ")
    y += 1

print("\n")

a = 0
while a < 10:
    b = 0
    while b < 5:
        print(f"({a + 1}|{b + 1})")
        b += 1
    a += 1
