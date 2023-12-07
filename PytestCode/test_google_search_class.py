import pytest
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("setup")
class TestGoogleSearch:
    def test_google_search_data(self):
        self.driver.get("https://google.co.in")
        self.driver.find_element(By.NAME, "q").send_keys("Learning Selenium")
        self.driver.find_element(By.NAME, "btnK").click()
        time.sleep(5)
