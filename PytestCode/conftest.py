import pytest
from selenium import webdriver

@pytest.fixture(scope='module')
def greeting():
    print(" --- Hello Good Morning Lets start the execution --")
    yield
    print("-- end of the test execution --")


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver