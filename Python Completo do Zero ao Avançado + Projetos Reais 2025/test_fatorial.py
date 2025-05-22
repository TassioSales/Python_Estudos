import pytest
from fatorial_logging import fatorial

def test_fatorial_zero():
    """Testa o fatorial de 0"""
    assert fatorial(0) == 1

def test_fatorial_um():
    """Testa o fatorial de 1"""
    assert fatorial(1) == 1

def test_fatorial_cinco():
    """Testa o fatorial de 5"""
    assert fatorial(5) == 120

def test_fatorial_dez():
    """Testa o fatorial de 10"""
    assert fatorial(10) == 3628800

def test_fatorial_numero_negativo():
    """Testa se o fatorial de número negativo lança ValueError"""
    with pytest.raises(ValueError):
        fatorial(-1)

def test_fatorial_performance():
    """Testa o fatorial com números grandes"""
    assert fatorial(20) == 2432902008176640000
    assert fatorial(30) == 265252859812191058636308480000000

def test_fatorial_recursao():
    """Testa o fatorial com números que exigem muita recursão"""
    assert fatorial(15) == 1307674368000
    assert fatorial(25) == 15511210043330985984000000
