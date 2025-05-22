def maior_primo(n):
    """
    Recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função.
    """
    def eh_primo(k):
        if k < 2:
            return False
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return False
        return True
    
    for i in range(n, 1, -1):
        if eh_primo(i):
            return i
    return None
