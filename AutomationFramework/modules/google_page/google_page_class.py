from base.selenium_base import SeleniumBase
from .google_page_locator import *


class GooglePage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_google_page(self, url):
        self.driver.get(url)

    def enter_value_to_search_box(self, search_content):
        self.enter_text(search_content, google_search_box_locator)

    def click_search_button(self):
        self.click_element(google_search_button_locator)
