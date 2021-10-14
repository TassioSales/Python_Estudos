def divide(n1,n2):
    if n2 == 0:
        raise ValueError
    return n1 / n2


try:
    print(divide(2, 0))
except ValueError as erro:
    print(erro.__class__)
