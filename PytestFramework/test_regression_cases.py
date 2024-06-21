"""
pip install pytest
"""

"""
fixture scope:
function : function level execute with each test function
module : module level works with each module.
package : package level works for multiple modules in the package, package scope has higher priority then module.
session : session level scope works with execution session to execute all test packages.
class : class level scope with each class setup and teardown

# session -> package -> module -> function

# session -> package -> module -> class -> function


"""

import pytest


@pytest.mark.smoke
def test_function4():
    num1 = 10
    num2 = 20
    assert num1 + num2 == 30


@pytest.mark.sanity
def test_function5():
    num1 = 10
    num2 = 20
    assert num1 * num2 == 200


@pytest.mark.regression
def test_function6():
    num1 = 10
    num2 = 20
    assert num1 - num2 == 40
