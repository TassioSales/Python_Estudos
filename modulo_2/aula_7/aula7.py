d1 = {"chave1":"Valor da chave"}
d1['nova_chave'] = "Valor da nova chave"

print(d1)

d2 = dict(chave1 = "valor da chave", chave2 = "Valor da chave 2")


print(d2)

d3 = {
    "str":"Valor",
    123:"Outro valor",
    (1,2,3,4) : "Tupla"
}
d3.get("str")
d3.update({123:456})

print(d3)

print("str" in d3)
print("str" in d3.keys())
print("Valor" in d3.values())

d5 = {
    "chave1": "valor",
    "chave2": "Outro Valor",
    "chave3": "Tupla"
}

for k, v in d5.items():
    print(k, v)