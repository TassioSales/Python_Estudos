import sys
import time


# lista = list(range(1000))
#
# print(lista)
#
# print(sys.getsizeof(lista))


def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r


g = gera()

for v in g:
    print(v, end=" ")
