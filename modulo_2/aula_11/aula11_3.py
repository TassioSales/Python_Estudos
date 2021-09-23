def gera():
    var = "valor 1"
    yield var
    var = "valor 2"
    yield var
    var = "valor 3"
    yield var

g = gera()

print(next(g))
print(next(g))
print(next(g))

