from types import GeneratorType

variavel = ((x, y) for x, y in zip("Alo", "Alo"))

print(isinstance(variavel, GeneratorType))

print(list(variavel))