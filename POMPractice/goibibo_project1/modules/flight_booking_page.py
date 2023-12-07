from resource import flight_booking_page_data as data
from basemodule.basefile import SeleniumDriver
from resource import session_data as session_data
from selenium.webdriver.common.by import By
from utilities.get_logger import logger

class BookFlight(SeleniumDriver):
    def __init__(self, driver):
        super(BookFlight, self).__init__(driver)

    def close_singup_popup(self):
        logger.info(f"{data.close_icon_singup_popup}")
        self.click_element(data.close_icon_singup_popup)


    def enter_value_for_source_city(self, src_city):
        self.click_element(data.from_city_placeholder)
        self.send_data_field(src_city, data.from_city_input_box)
        xpath_drop_down = (By.XPATH, f"//span[contains(text(), '{src_city}')]//ancestor::li")
        self.click_element(xpath_drop_down)

    def enter_value_for_destination_city(self, dest_city):
        self.send_data_field(dest_city, data.to_city_input_box)
        xpath_drop_down = (By.XPATH, f"//span[contains(text(), '{dest_city}')]//ancestor::li")
        self.click_element(xpath_drop_down)

    def select_departure_date(self, dpart_date):
        depart_date_xpath = (By.XPATH, f"//div[@aria-label='{dpart_date}']")
        self.click_element(depart_date_xpath)
        self.click_element(data.depart_date_done_button)

    def select_passenger_details(self, adults=1, child=0, infants=0, travel_class='Economy'):
        for _ in range(1, adults):
            self.click_element(data.adult_plus_icon)

        for _ in range(child):
            self.click_element(data.children_plus_icon)

        for _ in range(infants):
            self.click_element(data.infants_plus_icon)

        travel_class_xpath = (By.XPATH, f"//li[text()='{travel_class.lower()}']")
        self.click_element(travel_class_xpath)
        self.click_element(data.passenger_details_done_button)

    def click_to_search_button(self):
        self.click_element(data.search_button)







