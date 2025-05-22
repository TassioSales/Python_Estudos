def maximo(n1, n2):
    """
    Recebe dois números inteiros e retorna o maior deles.
    """
    return max(n1, n2)

def maior_primo(n):
    """
    Recebe um número inteiro >= 2 e retorna o maior número primo <= n.
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

def vogal(caractere):
    """
    Recebe um caractere e retorna True se for vogal, False se for consoante.
    """
    vogais = 'aeiouAEIOU'
    return caractere in vogais
