from itertools import combinations, permutations, product

pessoas = ['Tassio', "Lucian", "Jesus", "Sales", "Julia", "Santos", "Vasco", "Mendonca"]

print("###COMBINATIONS###")
print()

for grupo in combinations(pessoas, 3):
    print(grupo)

print()
print("###PERMUTATIONS###")
print()

for grupo in permutations(pessoas, 3):
    print(grupo)

print()
print("###PRODUCT###")
print()

for grupo in product(pessoas, repeat=3):
    print(grupo)

