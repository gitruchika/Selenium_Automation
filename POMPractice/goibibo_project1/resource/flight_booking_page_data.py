from selenium.webdriver.common.by import By

from_city_placeholder = (By.XPATH, "//span[text()='From']//following-sibling::p[contains(text(), 'Enter city or "
                                   "airport')]")
from_city_input_box = (By.XPATH, "//span[text()='From']//following-sibling::input")
to_city_placeholder = (By.XPATH, "//span[text()='To']//following-sibling::p[contains(text(), 'Enter city or airport')]")
to_city_input_box = (By.XPATH, "//span[text()='To']//following-sibling::input")
depart_date_done_button = (By.XPATH, "//span[text()='Done']")
adult_plus_icon = (By.XPATH, "//p[text()='Adults']//parent::div//span[3]")
children_plus_icon = (By.XPATH, "//p[text()='Children']//parent::div//span[3]")
infants_plus_icon = (By.XPATH, "//p[text()='Infants']//parent::div//span[3]")
passenger_details_done_button = (By.XPATH, "//a[text()='Done']")
search_button = (By.XPATH, "//span[text()='SEARCH FLIGHTS']")
close_icon_singup_popup = (By.XPATH, "//span[@class='logSprite icClose']//parent::span")


