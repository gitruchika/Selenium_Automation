import pytest


@pytest.mark.smoke
def test_flight_first_validation():
    num1 = 50
    num2 = 40
    assert num1 == num2

@pytest.mark.smoke
@pytest.mark.sanity
def test_flight_second_validation():
    num1 = 20
    assert num1*2 == 40

@pytest.mark.sanity
def test__flight_third_validation():
    num1 = 60
    num2 = 70
    assert num1+num2 == 130

@pytest.mark.sanity
def test_flight_fourth_validation():
    num1 = 50
    num2 = 40
    assert num1 == num2

@pytest.mark.regression
def test_flight_fifth_validation():
    num1 = 20
    assert num1*2 == 40

@pytest.mark.regression
def test_flight_sixth_validation():
    num1 = 60
    num2 = 70
    assert num1+num2 == 130
