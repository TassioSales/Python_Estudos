def fizzbuzz(n):
    """
    Recebe um número inteiro e retorna:
    'Fizz' se divisível por 3 e não por 5
    'Buzz' se divisível por 5 e não por 3
    'FizzBuzz' se divisível por 3 e 5
    Retorna o próprio número se não for divisível por 3 ou 5
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return n
