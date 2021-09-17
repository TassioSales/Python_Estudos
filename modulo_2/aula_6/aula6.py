t1 = (1,2,3,"a", "Tassio Sales")

print(type(t1))

for v in t1:
    print(v)

print(t1[2:5])

t2 = 1,2,3,4,5
t3 = 6,7,8,9,10
t3 = t2 + t3


n1, n2, n3,  *_,  n10 = t3

print(t3)
print(n1)

t5 = list(t3)
print(t5)