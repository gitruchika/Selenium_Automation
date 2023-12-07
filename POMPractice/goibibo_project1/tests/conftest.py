from basemodule.driver_factory import get_driver
import resource.session_data as session_data
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="session")
def browser(pytestconfig):
    return pytestconfig.getoption("browser")

@pytest.fixture(scope="class")
def launch_browser(request, browser):
    if browser:
        driver = get_driver(session_data.dummy_website_url, browser)
    else:
        driver = get_driver(session_data.dummy_website_url, session_data.browser)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope="class")
def launch_browser_flight(request):
    driver = get_driver(session_data.url, session_data.browser)
    request.cls.driver = driver
    yield
    driver.close()


