from selenium.webdriver.common.by import By

web_site_header = (By.XPATH, "//h1[@align='center']")
booking_options = (By.XPATH, "//span[text()='option_value']//parent::li/input")
first_name_field = (By.XPATH, "(//input[@id='firstname'])[1]")
last_name_field = (By.XPATH, "(//input[@id='firstname'])[2]")
date_of_birth_field = (By.XPATH, "//input[@id='birthday']")
male_radio_button = (By.ID, "male")
female_radio_button = (By.ID, "female")
addition_passengers_dropdown = (By.ID, "admorepass")
one_way_radio_button = (By.ID, "oneway")
round_trip_radio_button = (By.ID, "roundtrip")
from_city_field = (By.ID, "fromcity")
destination_city_field = (By.ID, "destcity")
dpart_date_field = (By.ID, "departdate")
return_date_field = (By.ID, "returndate")
visa_interview_date_field = (By.ID, "visadate")
most_visite_city_checkbox = (By.XPATH, "//td[text()='city_id']//parent::tr//input")

