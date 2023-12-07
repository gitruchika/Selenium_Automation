import pytest



@pytest.mark.parametrize("num1, num2, num3", [(20, 40, 60),
                                              (30, 40, 80),
                                              (100, 300, 400),
                                                  (500, 600, 1100)])
def test_first_validation(num1, num2, num3):
    assert num1 + num2 == num3
