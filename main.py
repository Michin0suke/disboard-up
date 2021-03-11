import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
from time import sleep
import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

url = 'https://disboard.org/ja/dashboard/servers'

def main():
    options = Options()
    if hasattr(config, 'binary_location'):
        options.binary_location = config.binary_location
    options.add_argument('--headless')
    options.add_argument('window-size=1600,900')
    driver = webdriver.Chrome(options=options, executable_path=config.chrome_driver_path)

    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)

        email_form = wait.until(expected_conditions.visibility_of_element_located((By.NAME, 'email')))
        password_form = driver.find_element_by_name('password')
        submit_button = driver.find_element_by_css_selector('button[type=submit]')
        email_form.send_keys(config.email)
        password_form.send_keys(config.password)
        submit_button.click()

        sleep(3)

        verify_button = wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'lookFilled-1Gx00P')))
        if verify_button:
            verify_button.click()
        element = wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'button-bump')))
        driver.find_element_by_class_name('button-bump').click()
        sleep(10)

    except Exception as e:
        print(e)

    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()