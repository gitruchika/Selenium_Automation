import pytest

@pytest.fixture(scope ='function')
def setup():
    print("Code execution started")
    yield
    print("\n Code execution completed")

@pytest.mark.smoke
def test_addition(setup):
    a = 10
    b = 20
    assert a+b == 30
@pytest.mark.sanity
def test_sub(setup):
    i = 50
    j = 10
    assert i-j == 40
@pytest.mark.regression
def test_multiplication(setup):
    num1 = 20
    num2 = 10
    assert num1*num2 == 200








