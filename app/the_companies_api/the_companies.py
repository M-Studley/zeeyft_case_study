from time import sleep
from random import random, randint

import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver import ChromeOptions
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
    # Uncomment the following line for headless mode
    # options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    print('Initializing WebDriver...')
    return driver


def navigate_target_url(driver: selenium.webdriver.Chrome) -> None:
    """
    Navigates the WebDriver to the target URL.

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.
    """
    target_url = 'https://www.thecompaniesapi.com/companies'
    print(f'Navigating to {target_url}')
    driver.get(target_url)
    sleep(3 + random())


def cookie_manager(driver: selenium.webdriver.Chrome) -> None:
    """
    Adds predefined cookies to the WebDriver session to manage authentication or session state.

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.
    """
    print('Adding Cookies...')
    driver.add_cookie(
        {'name': 'opaqueToken',
         'value': 'oat_MzMxOA.NGlCdDFMRllzR2Nha1VXc3hhWlNoRDd2VUg4dTVIVHZnaFlqVFZRdTE4Nzk0MTk2Njg'})
    sleep(random())
    driver.add_cookie(
        {'name': 'crisp-client%2Fsession%2Ff27054a5-2157-4277-a935-a2e40ca00dc1',
         'value': 'session_b895a9f0-b12a-4e4d-97a9-f7b47766cc04'})
    sleep(random())
    driver.add_cookie(
        {'name': '_GRECAPTCHA',
         'value': '09AIShAI25ouLfKp-aBR2uOtg8CgKw9dKQlgnxsXhhMRLMjvTc_nNGbkatsWJ99D9GrkWBgQ05Xnu9Kt9juS4U7bE'})
    sleep(random())

def random_email_generator() -> str:
    """
    Generates a random email address for testing purposes.
    Currently, not in use.

    Returns:
        str: A randomly generated email address.
    """
    random_email = ''
    for i in range(14 + 1):
        random_email += chr(randint(97, 122))

    return random_email + '@gmail.com'


def login_manager(driver: selenium.webdriver.Chrome) -> None:
    """
    Manages the login process by inputting an email and password into the login form fields and submitting the form.

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.
    """
    email = 'copperfox008@gmail.com'
    password = 'copperfox008'
    sleep(5 + random())
    login_email_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, 'n9EIb1D2ANG-4')
        )
    )
    login_email_field.click()
    for char in email:
        login_email_field.send_keys(char)
        sleep(random())

    login_password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, 'n9EIb1D2ANG-5')
        )
    )
    login_password_field.click()
    for char in password:
        login_password_field.send_keys(char)
        sleep(random())

    print('Logging In User...')
    sleep(random())
    login_password_field.send_keys(Keys.RETURN)
    sleep(65 + random())


def search_field_manager(driver: selenium.webdriver.Chrome, search_inputs: list[str], tag_id: str) -> None:
    """
    Manages the input of search terms into a specified search field and submits the search.

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.
        search_inputs (list[str]): A list of search terms to input.
        tag_id (str): The ID of the search field.
    """
    if tag_id != 'group relative flex h-10':
        search_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, tag_id)
            )
        )
    else:
        search_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
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

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.
    """
    print('Toggling "or" button to "and"...')
    or_to_and_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
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

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.
    """
    new_condition_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'div.base-icon.flex.flex-row.items-center.cursor-pointer.hover\\:underline')
        )
    )
    new_condition_btn.click()
    sleep(1 + random())

    new_condition_pull_down = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//div[contains(@class, 'flex items-center gap-2 mb-1.5')]//span[text()='Monthly visitors']")
        )
    )
    new_condition_pull_down.click()
    sleep(1 + random())

    country_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//div[@class='absolute left-0 right-0 z-10 cursor-default bottom-0 translate-y-full']"
             "//span[text()='Country']")
        )
    )
    country_btn.click()
    sleep(1 + random())


def data_extraction(driver: selenium.webdriver.Chrome) -> list[dict]:
    print('Attempting Data Extraction...')
    elements = driver.find_elements(
        By.XPATH,
        value='//*[@id="__nuxt"]/div[2]/main/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]')
    print(elements)

    results = []
    for element in elements:
        div_counter = 2
        root_selector = f'//*[@id="__nuxt"]/div[2]/main/div[1]/div/div/div[2]/div[2]/div/div[1]/div[{div_counter}]'
        target_data = {}

        try:
            target_data['title'] = element.find_element(
                By.XPATH,
                value=f'{root_selector}/span[2]/div/div/span').text
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

        div_counter += 1

    return results


def execute_with_error_handling(func, *args, **kwargs) -> None:
    """
    Executes a given function with error handling for NoSuchElementException.

    Args:
        func (callable): The function to execute.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.
    """
    try:
        func(*args, **kwargs)
    except NoSuchElementException as e:
        print(f'{func.__name__} Failed! Exception: {str(e)}')


def main():
    """
    The main function orchestrates the entire scraping process.
    It initializes the WebDriver, navigates to the target URL, manages cookies, logs in, performs searches,
    toggles conditions, and adds new conditions.
    """
    driver = init_chrome_web_driver()
    try:
        navigate_target_url(driver=driver)
        cookie_manager(driver=driver)

        execute_with_error_handling(login_manager, driver)
        execute_with_error_handling(search_field_manager, driver,
                                    ['wine', 'import'],
                                    'n9EIb1D2ANG-3')
        execute_with_error_handling(or_to_and_btn_toggle, driver)
        execute_with_error_handling(add_new_condition_manager, driver)
        execute_with_error_handling(search_field_manager, driver,
                                    ['australia', 'china', 'poland', 'united kingdom', 'united states'],
                                    'group relative flex h-10')
        try:
            sleep(5 + random())
            results = data_extraction(driver=driver)
            try:
                df = pd.DataFrame(results)
                df.to_csv("Wine_Distributors.csv")
            except Exception as e:
                print(f'Failed! Exception: {e}')

            try:
                df = pd.DataFrame(results)
                df.to_excel("Wine_Distributors.xlsx")
            except Exception as e:
                print(f'Failed! Exception: {e}')

        except Exception as e:
            print(f'Data Extraction Failed! Exception: {e}')

    finally:
        print('Shutting Down WebDriver Session...')
        driver.quit()


if __name__ == '__main__':
    main()
