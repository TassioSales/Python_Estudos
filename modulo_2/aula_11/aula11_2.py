import time
import sys


def gera():
    r = []
    for n in range(100):
        yield n
        time.sleep(0.5)
    return r


g = gera()


print(g)

print(hasattr(g, '__iter__'))
print(hasattr(g, "__next__"))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


