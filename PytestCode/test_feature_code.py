import pytest

@pytest.mark.smoke
def test_addition():
    num1 = 60
    num2 = 50
    assert num1+num2 == 100

@pytest.mark.sanity
def test_multiplication():
    num1 = 7
    num2 = 60
    assert num1*num2 == 420

@pytest.mark.regression
def test_subtraction():
    num1 = 60
    num2 = 40
    assert num1 - num2 == 20