lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
lista3 = [1, 2, 3, 4, 5, "A", "B", "C", "D", "E"]

print(lista1)
print(lista2)
print(lista3)

print(lista1[0])
print(lista2[0])
print(lista3[0])

lista1[1] = "qual quer coisa"
lista2[2] = "qual quer coisa"
lista3[3] = "qual quer coisa"

print(lista1[1])
print(lista2[2])
print(lista3[3])

print(lista1[0:5])
print(lista1[2:4])
print(lista1[5:8])

print(lista1[::2])
print(lista1[::-1])

lt1 = [1, 2, 3]
lt2 = [4, 5, 6]

lt3 = lt1 + lt2

lt3.insert(0, "banana")
lt3.pop()
print(lt3)

del (lt3[2:5])

print(lt3)

lt4 = list(range(0, 100, 2))

for num in lt4:
    print(num, end= " ")
    print(num ** 2)

for num in lt4:
    print(f"O elemento {num} e do tipo {type(num)}")