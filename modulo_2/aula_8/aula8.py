s1 = {1, 2, 3, 4, 5}

for v in s1:
    print(v)

s2 = set()

s2.add(1)
s2.add(2)
s2.add((1, 2, 3, "luiz"))

s2.discard(2)
s2.update("python")

s3 = set()
s3.update([1, 2, 3, 4, 5], {5, 6, 7, 8, 9})
print(s3)
print(s2)


l1 = [1, 1, 1, 1, 2, 2 , 3, 4, 4, 4, "tassio", "tassio", 9, 9, 9, 6, 6, 6, 6, 6, 6, 6]
l1 = set(l1)
l1 = list(l1)
print(l1)

set1 = {1, 2, 3, 4, 5, 7}
set2 = {1, 2, 3, 4, 5, 6}
set3 = set1 | set2
set4 = set1 & set2
set5 = set1 - set2
set6 = set1 ^ set2
print(set3)
print(set4)
print(set5)
print(set6)
      



