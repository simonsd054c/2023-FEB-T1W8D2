# assertion - assert
import pytest
from calculator import add, subtract, division, convert_into_list

def test_basic():
    assert "hello" == "hello"

def test_add():
    assert add(3, 1) == 4
    assert add(5, 4) == 9

def test_subtract():
    assert subtract(8, 5) == 3
    assert subtract(10, 5) == 5
    assert subtract(-5, -3) == -2

def test_division():
    assert division(10, 5) == 2.0

def test_division_raising_error():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)

def test_convert():
    assert 5 in convert_into_list(3, 4, 5)
    assert 10 not in convert_into_list(3, 4, 5)