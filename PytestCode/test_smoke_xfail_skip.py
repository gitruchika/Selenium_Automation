import pytest


env = 'PROD'

@pytest.mark.smoke
@pytest.mark.xfail
def test_first_validation(greeting):
    num1 = 50
    num2 = 40
    assert num1 == num2

@pytest.mark.smoke
def test_second_validation(greeting):
    num1 = 20
    assert num1*2 == 40


@pytest.mark.sanity
def test_third_validation(greeting):
    num1 = 60
    num2 = 70
    assert num1+num2 == 130

@pytest.mark.sanity
@pytest.mark.skip
def test_fourth_validation(greeting):
    num1 = 50
    num2 = 40
    assert num1 == num2

@pytest.mark.regression
@pytest.mark.skipif(env == "PROD", reason="Can not execute in production environment")
def test_fifth_validation(greeting):
    num1 = 20
    assert num1*2 == 40

@pytest.mark.regression
@pytest.mark.skipif(env == "PROD", reason="Can not execute in production environment")
def test_sixth_validation(greeting):
    num1 = 60
    num2 = 70
    assert num1+num2 == 130
