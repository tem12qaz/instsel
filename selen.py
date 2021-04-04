import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import NAMES
from funcs import parse_inst

browser = webdriver.Chrome()

browser.get('https://www.instagram.com/_rl9/')
# x = browser.find_element_by_class_name('g47SY').get_attribute('title')
try:
    elem = WebDriverWait(browser, 3).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "_2hvTZ"))
    )
    elem[0].send_keys('timonf9')
    elem[1].send_keys('%p!k5Z]3::oUy@A' + Keys.ENTER)
    time.sleep(10)
    xlsx = parse_inst(NAMES, browser)
finally:
    pass