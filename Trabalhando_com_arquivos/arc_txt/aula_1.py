file = open('abc.txt', 'w+')
for i in range(1, 4):
    file.write(f"Linha {i} \n")
file.seek(0, 0)
print("Lendo Linhas")
print(file.read())

print("############################")
file.seek(0, 0)
print(file.readline(), end ='')
print(file.readline(), end ='')
print(file.readline(), end ='')

print("############################")

file.seek(0, 0)
print(file.readlines())

file.seek(0, 0)

for linha in file.readlines():
    print(linha, end="")
print("\n")
file.seek(0, 0)

for linha in file:
    print(linha, end="")


file.close()
