from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=20)

    def get_element(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def enter_text(self, data, locator):
        element = self.get_element(locator)
        element.send_keys(data)

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def select_dropdown_value(self, value, locator):
        element = self.get_element(locator)
        obj = Select(element)
        obj.select_by_visible_text(value)

