from time import sleep
from random import random

import csv
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utils.utils import (init_chrome_web_driver,
                         navigate_target_url,
                         scroll_by_delta_x_and_y,
                         execute_with_error_handling,
                         Pagination)


def login_manager(driver: selenium.webdriver.Chrome, credentials: dict) -> None:
    """
    Manages the login process by inputting an email and password into the login form fields and submitting the form.
    For testing purposes please use email = 'copperfox008@gmail.com' password = 'copperfox008'

    :param driver: The WebDriver instance currently in use.
    :param credentials: dictionary of two key value pairs: email , password
    """
    login_email_field = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.ID, 'n9EIb1D2ANG-4')
        )
    )
    login_email_field.click()
    for char in credentials['email']:
        login_email_field.send_keys(char)
        sleep(random() / 2)

    login_password_field = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.ID, 'n9EIb1D2ANG-5')
        )
    )
    login_password_field.click()
    for char in credentials['password']:
        login_password_field.send_keys(char)
        sleep(random() / 2)

    print('Logging In User...')
    sleep(random())
    login_password_field.send_keys(Keys.RETURN)
    sleep(65 + random())


def search_field_manager(driver: selenium.webdriver.Chrome, search_inputs: list[str], tag_id: str) -> None:
    """
    Manages the input of search terms into a specified search field and submits the search.

    :param driver: (selenium.webdriver.Chrome) The WebDriver instance currently in use.
    :param search_inputs: (list[str]) A list of search terms to input.
    :param tag_id: (str) The ID of the search field.
    """
    if tag_id != 'group relative flex h-10':
        search_field = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable(
                (By.ID, tag_id)
            )
        )
    else:
        search_field = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable(
                (By.XPATH, '//div[contains(@class, "group relative flex h-10")]//input')
            )
        )
    search_field.click()

    for search_input in search_inputs:
        print(f'Inputting {search_input}...')
        sleep(random())
        for char in search_input:
            search_field.send_keys(char)
            sleep(random())
        search_field.send_keys(Keys.RETURN)
    sleep(1 + random())


def or_to_and_btn_toggle(driver: selenium.webdriver.Chrome) -> None:
    """
    Toggles a button to change the search condition from "or" to "and".

    :param driver: (selenium.webdriver.Chrome) The WebDriver instance currently in use.
    """
    print('Toggling "or" button to "and"...')
    or_to_and_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'div[class="base-tags flex items-center flex-wrap justify-start -ml-1 -mt-1 mb-1"] '
             '> span > span:nth-child(2) > div')
        )
    )
    or_to_and_button.click()
    sleep(1 + random())


def add_new_condition_manager(driver: selenium.webdriver.Chrome) -> None:
    """
    Adds a new condition to the search by interacting with the necessary UI elements.

    :param driver: (selenium.webdriver.Chrome) The WebDriver instance currently in use.
    """
    new_condition_btn = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'div.base-icon.flex.flex-row.items-center.cursor-pointer.hover\\:underline')
        )
    )
    print('Clicking "Add a new condition" Button...')
    new_condition_btn.click()
    sleep(1 + random())

    new_condition_pull_down = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.XPATH,
             "//div[contains(@class, 'flex items-center gap-2 mb-1.5')]//span[text()='Monthly visitors']")
        )
    )

    print('Clicking New Condition Pull Down Menu...')
    new_condition_pull_down.click()
    sleep(1 + random())

    locate_country_btn = driver.find_element(
        By.XPATH,
        value="//div[@class='absolute left-0 right-0 z-10 cursor-default "
              "bottom-0 translate-y-full']//span[text()='Country']")

    scroll_by_delta_x_and_y(driver=driver,
                            coord=(0, 200))

    country_btn = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(locate_country_btn)
    )
    print('Clicking "Country" Button...')
    country_btn.click()
    sleep(1 + random())


def data_extraction(driver: selenium.webdriver.Chrome) -> list[dict]:
    """
    Extracts data from the web page using Selenium WebDriver.

    This function attempts to find specific elements on the web page and extracts relevant data such as title, URL,
    revenue, number of employees, country, region, city/state, and LinkedIn URL. The extracted data is stored in a
    dictionary and appended to a results list.

    :param driver: (selenium.webdriver.Chrome) The WebDriver instance currently in use.

    :return list[dict]: A list of dictionaries, each containing extracted data for a company.
    """
    print('Attempting Data Extraction...')
    element = driver.find_element(
        By.XPATH,
        value='//*[@id="__nuxt"]/div[2]/main/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]')

    results = []
    for page in range(4):
        sleep(2 + random())
        for i in range(2, 25 + 2):
            target_data = {}
            root_selector = f'//*[@id="__nuxt"]/div[2]/main/div[1]/div/div/div[2]/div[2]/div/div[1]/div[{i}]'

            try:
                first_element = WebDriverWait(driver, 10).until(
                    ec.element_to_be_clickable(
                        (By.XPATH,
                         f'{root_selector}/span[2]/div/div/span')
                    )
                )
                target_data['title'] = first_element.text
            except Exception:
                target_data['title'] = 'None'

            try:
                target_data['url'] = element.find_element(
                    By.XPATH,
                    value=f'{root_selector}/span[2]/div/a').get_attribute('href')
            except Exception:
                target_data['url'] = 'None'

            try:
                target_data['revenue'] = element.find_element(
                    By.XPATH,
                    value=f'{root_selector}/span[4]/span/span').text
            except Exception:
                target_data['revenue'] = 'None'

            try:
                target_data['employees'] = element.find_element(
                    By.XPATH,
                    value=f'{root_selector}/span[5]/span/span').text
            except Exception:
                target_data['employees'] = 'None'

            try:
                target_data['country'] = element.find_element(
                    By.XPATH,
                    value=f'{root_selector}/span[7]/div/div[1]/div[2]/span').text
            except Exception:
                target_data['country'] = 'None'

            try:
                target_data['region'] = element.find_element(
                    By.XPATH,
                    value=f'{root_selector}/span[8]/div/div[1]/span').text
            except Exception:
                target_data['region'] = 'None'

            try:
                target_data['city,state'] = element.find_element(
                    By.XPATH,
                    value=f'{root_selector}/span[8]/div/div[2]/div/span').text
            except Exception:
                target_data['city,state'] = 'None'

            try:
                target_data['linkedin_url'] = element.find_element(
                    By.XPATH,
                    value=f'{root_selector}/span[10]/div/div[1]/a').get_attribute('href')
            except Exception:
                target_data['linkedin_url'] = 'None'

            if target_data.get('title') != 'None':
                results.append(target_data)

            Pagination.click_next_page_button(driver=driver,
                                              coord=(0, 2323),
                                              css_selector='div[class="flex flex-1 items-center justify-center"] > '
                                                           'div:nth-child(3)')

    return results


def main():
    """
    The main function orchestrates the entire scraping process.
    It initializes the WebDriver, navigates to the target URL, manages cookies, logs in, performs searches,
    toggles conditions, and adds new conditions.
    """
    driver = init_chrome_web_driver()
    # cookies = [
    #     {'name': 'opaqueToken',
    #      'value': 'oat_MzMzNQ.QVJZWDRjdjRoczQya2t0bmFsWkdjaTZnZnJuWmVTYTlDaDl3VmNwazI4MDYwNzg5ODg'},
    #     {'name': 'crisp-client%2Fsession%2Ff27054a5-2157-4277-a935-a2e40ca00dc1',
    #      'value': 'session_be399813-e046-414e-9eaa-b9b3c42ab14f'},
    #     {'name': '_hjSession_2840334',
    #      'value': 'eyJpZCI6ImUxYWJhYTgyLWNkNTMtNDBjNi1hNzdjLTI4ZjQ2OGM1NTUxOCIsImMiOjE3MjE1Nj'
    #               'IwODQxNTYsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0='},
    #     {'name': '_hjSessionUser_2840334',
    #      'value': 'eyJpZCI6IjE5MjI4Nzc5LTIwMGYtNTNiMC05NzFjLTc5ODVmM2VhYjhiYS'
    #               'IsImNyZWF0ZWQiOjE3MjE1NjIwODQxNTUsImV4aXN0aW5nIjp0cnVlfQ=='}
    # ]

    try:
        navigate_target_url(driver=driver,
                            target_url='https://www.thecompaniesapi.com/companies')

        # cookie_manager(driver=driver,
        #                cookies=cookies)

        execute_with_error_handling(login_manager,
                                    driver=driver,
                                    credentials={'email': 'copperfox008@gmail.com',
                                                 'password': 'copperfox008'})

        execute_with_error_handling(search_field_manager,
                                    driver=driver,
                                    search_inputs=['wine', 'import'],
                                    tag_id='n9EIb1D2ANG-3')

        execute_with_error_handling(or_to_and_btn_toggle,
                                    driver=driver)

        execute_with_error_handling(add_new_condition_manager,
                                    driver=driver)

        execute_with_error_handling(search_field_manager,
                                    driver=driver,
                                    search_inputs=['australia', 'china', 'poland', 'united kingdom', 'united states'],
                                    tag_id='group relative flex h-10')

        try:
            results = data_extraction(driver=driver)
        except Exception as e:
            print(f'Data Extraction Failed! Exception: {e}')

    finally:
        print('Shutting Down WebDriver Session...')
        driver.quit()

    try:
        fieldnames = [key.title() for key in results[0]]  # noqa
        with open('Wine_Distributors.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print('Creating CSV File...')
    except Exception as e:
        print(f'Failed! Exception: {e}')


if __name__ == '__main__':
    main()
