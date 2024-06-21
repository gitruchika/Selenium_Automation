"""
pip install pytest
"""
import pytest

env = "TEST"


class TestFeature:

    def test_function_zero(self):
        print("")

    @pytest.mark.smoke
    def test_function1(self):
        num1 = 10
        num2 = 20
        assert num1 + num2 == 30

    @pytest.mark.sanity
    @pytest.mark.skip
    def test_function2(self):
        num1 = 10
        num2 = 20
        assert num1 * num2 == 200

    @pytest.mark.regression
    @pytest.mark.skipif(env == "PROD", reason="Can not execute on product environment")
    def test_function3(self):
        num1 = 10
        num2 = 20
        assert num1 - num2 == 40
