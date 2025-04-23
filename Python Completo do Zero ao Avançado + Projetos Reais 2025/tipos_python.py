"""
tipos_python.py

Este módulo demonstra o uso de tipagem em Python e os principais erros
que ocorrem quando tipos incorretos são usados: TypeError e ValueError.
Inclui exemplos de soma entre int e str, conversão de tipos e tratamento de exceções.
"""
from typing import Any

def soma_int(a: int, b: int) -> int:
    """Retorna a soma de dois inteiros."""
    return a + b


def soma_str(a: str, b: str) -> str:
    """Concatena duas strings."""
    return a + b


def soma_int_e_str_sem_tratamento(a: int, b: str) -> int:
    """
    Tenta somar int com str sem conversão.
    Isso gera TypeError em tempo de execução.
    """
    return a + b  # TypeError


def soma_int_e_str_com_conversao(a: int, b: str) -> int:
    """
    Converte a string para int antes de somar.
    Se b não for string numérica, gera ValueError.
    """
    return a + int(b)


def exemplo_erros() -> None:
    """Mostra exemplos de erros de tipo e de valor."""
    x: int = 10
    y_str: str = "5"
    bad_str: str = "abc"

    print("Exemplo correto:", soma_int(x, int(y_str)))

    # TypeError: int + str
    try:
        print("Tentando soma sem conversão:")
        soma_int_e_str_sem_tratamento(x, y_str)
    except TypeError as err:
        print("TypeError capturado:", err)

    # ValueError: conversão de string não numérica
    try:
        print("Tentando conversão inválida:")
        soma_int_e_str_com_conversao(x, bad_str)
    except ValueError as err:
        print("ValueError capturado:", err)

if __name__ == "__main__":
    exemplo_erros()
