import pytest
from modules.flight_booking_page import BookFlight
from time import  sleep
from resource.test_data import *

@pytest.mark.usefixtures("launch_browser_flight")
class TestBookFlight:
    def test_book_flight_check(self):
        self.bf = BookFlight(self.driver)
        self.bf.close_singup_popup()
        self.bf.enter_value_for_source_city(source_location)
        self.bf.enter_value_for_destination_city(dest_location)
        self.bf.select_departure_date(departure_date)
        self.bf.select_passenger_details()
        sleep(5)
        self.bf.click_to_search_button()
        sleep(5)

