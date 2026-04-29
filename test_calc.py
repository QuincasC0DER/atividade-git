import pytest
from calc import soma, divide

def test_soma():
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-1, -1) == -2

def test_divide():
    assert divide(10, 2) == 5

def test_divide_por_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
