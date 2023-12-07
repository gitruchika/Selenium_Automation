from selenium import webdriver
from resource import session_data as session_data
from utilities.get_logger import logger, log_dir_path
from selenium.webdriver.chrome.options import Options

log = logger

def get_driver(url, browser):
    if browser.lower() == 'chrome':
        chrome_option = Options()
        if session_data.headless:
            chrome_option.add_argument("--headless")
        if session_data.incognito:
            chrome_option.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_option)
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(url)
        log.info(f"url successfully launched: {url}")
        return driver
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(session_data.global_timeout)
        driver.get(url)
        return driver
    elif browser.lower() == 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.implicitly_wait(session_data.global_timeout)
        driver.get(url)
        return driver

