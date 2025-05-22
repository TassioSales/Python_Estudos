def leitura():
    x = -1
    while x > 0:
        x = int(input("Digite um valor: "))
    return x 

print(leitura())


# o que a funcao leitura faz?
# a funcao leitura le um valor do usuario e retorna ele

# entao pq o resultado e -1?
# porque o while e while x > 0, ou seja, enquanto x for maior que 0, ele vai continuar lendo
# e como o valor e -1, ele nao entra no while
# logo, ele retorna -1



