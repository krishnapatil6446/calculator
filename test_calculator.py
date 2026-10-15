import pytest    #importing pytest
from calculator import add, subtract, multiply, divide, power, modulo

def test_add():                #for addition
    assert add(5, 3) == 8
    assert add(-1, 1) == 0


def test_subtract():            #for subtraction
    assert subtract(10, 2) == 8
    assert subtract(5, 5) == 0


def test_multiply():            #for multiplication
    assert multiply(4, 5) == 20
    assert multiply(5, 0) == 0


def test_divide():              #for division
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5


def test_divide_by_zero():      #divison by zero
    with pytest.raises(ValueError):
        divide(10, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(4, 1) == 4


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(5, 5) == 0
    assert modulo(7, 2) == 1


def test_modulo_by_zero():
    with pytest.raises(ValueError):
        modulo(10, 0)
