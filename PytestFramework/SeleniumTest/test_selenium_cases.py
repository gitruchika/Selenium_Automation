import time

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("selenium_setup")
class TestGoogleSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.ch_driver = self.driver

    def test_search_on_google(self):
        self.ch_driver.find_element(By.NAME, "q").send_keys("Python Selenium")
        self.ch_driver.find_element(By.NAME, "btnK").click()
        time.sleep(10)
