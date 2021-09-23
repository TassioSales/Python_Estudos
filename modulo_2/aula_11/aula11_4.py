import sys
import time

l1 = [x for x in range(100000)]

l2 = (x for x in range(100000))
print(type(l1))
print(type(l2))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

for c in l2:
    print(c)
