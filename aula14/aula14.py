"""
formatando valores com modificadores
"""

num_1 = 10
num_2 = 3

divisao = num_1 / num_2

print(divisao)
print("{:.2f}".format(divisao))
print(f'{divisao:.2f}')

nome = "Tassio Sales"

print(f'{nome:s}')

print(f"{nome:#^36}")
print(f"{nome.upper()}")
print(f"{nome.lower()}")
print(f"{nome.title()}")

num_3 = 4
num_4 = 8

soma = num_3 + num_4

print(f"{soma:d}")
print(f"{soma:0>10}")
print(f"{soma:0<10}")
