import pytest
from modules.dummy_website_page import DummyWebsite
from time import  sleep
from resource.test_data import *


@pytest.mark.usefixtures("launch_browser")
class TestDummyWebsite:
    """
    1. verify website header.
    2. Choose ticket option and verify
    3. Enter passenger details successfully.
    4. Choose number of addition passenger.
    5. Enter travel details
    6. Enter deliver option.
    7. Enter billing details and verify
    8. Select most visited city.
    """
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)

    def test_verify_website_header(self):
        header_name = self.dw.get_website_header()
        assert header_name == dummy_website_header

    def test_select_booking_option_and_verify(self):
        assert self.dw.choose_booking_option(booking_option)
        sleep(5)


