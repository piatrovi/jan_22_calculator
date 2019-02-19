"""
Test divide function
"""
import math
import pytest

from calculator import divide

def test_without_parameters():
    """
    Given that no parameters are provided
    to the function. Return float nan """
    assert divide() is math.nan

def test_divided_by_two():
    """Given hat parameters 4 and 2 are provided to the function
    and 2 should return """
    assert divide(4, 2) == pytest.approx(2)

def test_divided_by_nothing():
    """
    Given that the value 3 is provided
    """
    assert divide(3) == 1

def test_divided_by_three_parameters():
    """Given hat parameters 100, 5 and  are provided to the function
    and 5 should return """
    assert divide(100, 5, 4) == pytest.approx(5)

def test_zero_division():
    """ Test zero division"""
    assert divide(2, 0) is math.nan
