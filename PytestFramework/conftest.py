import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By



@pytest.fixture(scope="function", autouse=True)
def setup():
    print("\n function execution started")
    yield
    print("\n function execution completed")


@pytest.fixture(scope="module", autouse=True)
def module_setup():
    print("\n module execution started")
    yield
    print("\n module execution completed")


@pytest.fixture(scope="package", autouse=True)
def package_setup():
    print("\n package execution started")
    yield
    print("\n package execution completed")


@pytest.fixture(scope="session", autouse=True)
def session_setup():
    print("\n session execution started")
    yield
    print("\n session execution completed")



@pytest.fixture(scope="class")
def selenium_setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://google.co.in")
    request.cls.driver = driver
    yield
    driver.close()
