# Explicação sobre o tipo booleano em Python

# O tipo booleano em Python tem dois valores possíveis: True e False
print("Valores booleanos:")
print("True:", True)
print("False:", False)
print()

# Exemplo com for
print("Exemplo com for:")
for i in range(5):
    # Verifica se o número é par
    e_par = (i % 2 == 0)
    print(f"O número {i} é par?", e_par)
print()

# Exemplo com while
print("Exemplo com while:")
numero = 1
while numero <= 3:
    # Verifica se o número é maior que 2
    maior_que_dois = (numero > 2)
    print(f"O número {numero} é maior que 2?", maior_que_dois)
    numero += 1
print()

# Exemplos de comparações que resultam em booleanos
print("Exemplos de comparações:")
print("5 > 3:", 5 > 3)      # True
print("2 == 2:", 2 == 2)    # True
print("10 < 5:", 10 < 5)    # False
print("'a' == 'b':", 'a' == 'b')  # False
print()

# Exemplo de uso em condições
print("Exemplo de uso em condições:")
idade = 18
if idade >= 18:
    print("Maior de idade? True")
else:
    print("Maior de idade? False")

# Booleanos também podem ser usados em operações lógicas
print("\nOperações lógicas:")
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("not True:", not True)              # False
print("not False:", not False)            # True)
