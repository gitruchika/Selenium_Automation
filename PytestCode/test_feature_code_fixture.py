import pytest

#@pytest.fixture(scope="session")
#@pytest.fixture(scope="function")
@pytest.fixture(scope="module")
def setup():
    print("The code execution started")
    yield
    print("\n The code execution completed")

@pytest.mark.smoke
def test_addition(setup):
    #var1 = setup
    num1 = 60
    num2 = 50
    assert num1+num2 == 100

@pytest.mark.sanity
def test_multiplication(setup):
    num1 = 7
    num2 = 60
    assert num1*num2 == 420

@pytest.mark.regression
def test_subtraction(setup):
    num1 = 60
    num2 = 40
    assert num1 - num2 == 20