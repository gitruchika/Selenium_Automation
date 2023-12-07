from resource import dummy_website_page_data as data
from basemodule.basefile import SeleniumDriver
from resource import session_data as session_data
from selenium.webdriver.common.by import By
from utilities.get_logger import logger


class DummyWebsite(SeleniumDriver):
    def __init__(self, driver):
        super(DummyWebsite, self).__init__(driver)

    def get_website_header(self):
        return self.get_element_text(data.web_site_header)

    def choose_booking_option(self, option):
        option_xpath = (By.XPATH, f"//span[contains(text(),'{option}')]//parent::li/input")
        element = self.get_element(option_xpath)
        element.click()
        return element.is_selected()










