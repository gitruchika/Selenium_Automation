"""
pip install pytest
"""
import pytest

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


# @pytest.fixture(scope="function", autouse=True)
# def setup():
#     print("\n function execution started")
#     yield
#     print("\n function execution completed")
#
#
# @pytest.fixture(scope="module", autouse=True)
# def module_setup():
#     print("\n module execution started")
#     yield
#     print("\n module execution completed")
#
#
# @pytest.fixture(scope="package", autouse=True)
# def package_setup():
#     print("\n package execution started")
#     yield
#     print("\n package execution completed")
#
#
# @pytest.fixture(scope="session", autouse=True)
# def session_setup():
#     print("\n session execution started")
#     yield
#     print("\n session execution completed")
#

@pytest.mark.smoke
def test_function1():
    num1 = 10
    num2 = 20
    assert num1 + num2 == 30


@pytest.mark.sanity
def test_function2():
    num1 = 10
    num2 = 20
    assert num1 * num2 == 200


@pytest.mark.regression
def test_function3():
    num1 = 10
    num2 = 20
    assert num1 - num2 == 40
