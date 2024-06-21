import time

import pytest
from modules.google_page.google_page_class import GooglePage
from modules.google_page.google_page_test_data import *


@pytest.mark.usefixtures("get_driver")
class TestGooglePage:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.gp = GooglePage(self.driver)

    def test_search_on_google(self):
        self.gp.open_google_page(google_url)
        self.gp.enter_value_to_search_box(search_content)
        self.gp.click_search_button()
        time.sleep(10)
