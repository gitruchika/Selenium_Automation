from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from resource import session_data as session_data
from utilities.get_logger import logger, log_dir_path
import datetime

log = logger

class SeleniumDriver:
    def __init__(self, driver, timeout=10):
        self.timeout = timeout
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_element(self, locator):
        try:
            log.info(f"found element for locator: {locator}")
            element = self.wait.until(ec.presence_of_element_located(locator))
            return element
        except Exception as e:
            file_name = datetime.datetime.now().strftime("element_not_found_%Y_%m_%d_%H_%M_%S")
            log.info(f"saved screen shot: {file_name}")
            self.driver.save_screenshot(f"{log_dir_path}/{file_name}.png")
            raise e

    def click_element(self, locator):
        element = self.get_element(locator)
        # file_name = datetime.datetime.now().strftime("snapshot_%Y_%m_%d_%H_%M_%S")
        # element.screenshot(f"{log_dir_path}/{file_name}.png")
        element.click()
        log.info(f"clicked on element: {locator}")

    def send_data_field(self, data, locator):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(data)
        log.info(f"data entered: {locator}, {data}")

    def get_element_text(self, locator):
        element = self.get_element(locator)
        log.info(f"got text of element: {locator}, {element.text}")
        return element.text
