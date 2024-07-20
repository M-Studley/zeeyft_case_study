from time import sleep
from random import random, randint

import selenium
from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def init_chrome_web_driver() -> webdriver:
    """
    Initializes a Chrome WebDriver with specific options for language, headless, and maximized window.

    Returns:
        webdriver.Chrome: Configured Chrome WebDriver instance.
    """
    options = ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    print('Initializing WebDriver...')
    return driver


def navigate_target_url(driver: selenium.webdriver.Chrome) -> None:
    target_url = 'https://www.thecompaniesapi.com/companies'
    print(f'Navigating to {target_url}')
    driver.get(target_url)
    print('Adding Cookies...')
    driver.add_cookie(
        {'name': 'opaqueToken',
         'value': 'oat_MzI4OQ.c0p4V0tzMURTRVc3YV9VTzJUb0hhRDRtQk5rTmdVZDdpdHBaNS14ODM5MTM1OTY4Njk'})
    sleep(random())
    driver.add_cookie(
        {'name': 'crisp-client%2Fsession%2Ff27054a5-2157-4277-a935-a2e40ca00dc1',
         'value': 'session_2cb3433f-b096-439a-b472-2f5c7fdd4e07'})
    sleep(random())
    driver.add_cookie(
        {'name': '_hjSession_2840334',
         'value': 'eyJpZCI6ImE5NjdmMjY4LTY1NDQtNDEyOC1hZTU4LWUzZDJmN2NjMTAzMyIsImMiOjE3MjE0NDU0MDgxNDMsInMiOjAsInIiOj'
                  'AsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0='})
    sleep(random())
    driver.add_cookie(
        {'name': '_hjSessionUser_2840334',
         'value': 'eyJpZCI6IjdmMzVjMTU3LTFiMDctNWVlNy1iYWUxLWU1MzNlYzcwNTRiZSIsImNyZWF0ZWQiOjE3MjE0NDU0MDgxNDAsImV4aX'
                  'N0aW5nIjpmYWxzZX0='})
    sleep(4 + random())


def random_email_generator() -> str:
    random_email = ''
    for i in range(14 + 1):
        random_email += chr(randint(97, 122))

    return random_email+'@gmail.com'


def login_manager(driver: selenium.webdriver.Chrome) -> None:
    email = 'copperfox008@gmail.com'
    password = 'copperfox008'
    sleep(5 + random())
    login_email_field = driver.find_element(By.ID, value='n9EIb1D2ANG-4')
    login_password = driver.find_element(By.ID, value='n9EIb1D2ANG-5')

    login_email_field.click()
    for char in email:
        login_email_field.send_keys(char)
        sleep(random())

    login_password.click()
    for char in password:
        login_password.send_keys(char)
        sleep(random())

    print('Logging In User...')
    sleep(random())
    login_password.send_keys(Keys.RETURN)
    sleep(5 + random())


def industries_search_field_manager(driver: selenium.webdriver.Chrome) -> None:
    search_field_inputs = ['wine', 'import']
    search_field = driver.find_element(By.ID, value='n9EIb1D2ANG-3')

    for search_field_input in search_field_inputs:
        print(f'Inputting {search_field_input}...')
        search_field.click()
        sleep(random())
        for char in search_field_input:
            search_field.send_keys(char)
            sleep(random())
        search_field.send_keys(Keys.RETURN)

    sleep(5 + random())
    print('Toggling "or" button to "and"...')
    or_to_and_button = driver.find_element(
        By.CSS_SELECTOR,
        value='div[class="base-tags flex items-center flex-wrap justify-start -ml-1 -mt-1 mb-1"] '
              '> span > span:nth-child(2) > div')
    or_to_and_button.click()
    sleep(1 + random())


def add_new_condition_manager(driver: selenium.webdriver.Chrome) -> None:
    sleep(5 + random())
    new_condition_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                   'div.base-icon.flex.flex-row.items-center.cursor-pointer.hover\\:underline'))
    )
    new_condition_btn.click()
    sleep(2 + random())
    # new_condition_pull_down = driver.find_element(
    #     By.CLASS_NAME,
    #     value='flex items-center gap-2 mb-1.5')
    # # flex items-center gap-2 mb-1.5"] > div > div > div > div
    # print('Clicking new condition pull down...')
    # new_condition_pull_down.click()
    # sleep(1 + random())
    # country_btn = driver.find_element(
    #     By.CSS_SELECTOR,
    #     value='div[class="grid grid-cols-1 gap-2 sm:grid-cols-2"] > div:nth-child(2) > div:nth-child(5) > div')
    # print('Clicking "County" selection from pull down...')
    # country_btn.click()
    # sleep(1 + random())


def country_search_field_manager(driver: selenium.webdriver.Chrome) -> None:
    search_field_inputs = ['australia']
    search_field = driver.find_element(By.CSS_SELECTOR, value='n9EIb1D2ANG_5')

    # todo - one country at a time, scrape, input second country, remove first, repeat

    for search_field_input in search_field_inputs:
        print(f'Inputting {search_field_input}...')
        search_field.click()
        sleep(random())
        for char in search_field_input:
            search_field.send_keys(char)
            sleep(random())
        search_field.send_keys(Keys.RETURN)


def main():
    driver = init_chrome_web_driver()
    try:
        navigate_target_url(driver)
        try:
            login_manager(driver)
        finally:
            industries_search_field_manager(driver)
            sleep(2 + random())
            add_new_condition_manager(driver)
            sleep(1 + random())
            # country_search_field_manager(driver)
    finally:
        print('Shutting Down WebDriver Session...')
        driver.quit()


if __name__ == '__main__':
    main()
