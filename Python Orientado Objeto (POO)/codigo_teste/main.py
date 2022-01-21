from primeiro_teste import A

a1 = A()
a2 = A()
A.vc = "Alterado"

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)
print()

print(a1.vc)
print(a2.vc)
print(A.vc)