from time import sleep
from random import random, randint

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


def cookie_manager(driver: selenium.webdriver.Chrome) -> None:
    """
    Adds predefined cookies to the WebDriver session to manage authentication or session state.

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.
    """
    print('Adding Cookies...')
    driver.add_cookie(
        {'name': 'opaqueToken',
         'value': 'oat_MzI5MQ.Y2Q0S1hWQ0hKcDh6TmdIbGItZmxRWE1oalZ2aGp6U1FQd0U0WXk3RDM5ODA4MTYzOTM'})
    sleep(random())
    driver.add_cookie(
        {'name': 'crisp-client%2Fsession%2Ff27054a5-2157-4277-a935-a2e40ca00dc1',
         'value': 'session_8aaa4a60-bbd8-4921-98d0-8ed7200d7a36'})
    sleep(random())
    driver.add_cookie(
        {'name': '_hjSession_2840334',
         'value': 'eyJpZCI6ImM3MTA0MjgxLTQ4YmUtNDBkZi05ODM4LTUxMDU2NDAyOTNkZiIsImMiOjE3MjE0NTYzNDcyMTksInMiOjEsInIiOjEs'
                  'InNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0='})
    sleep(random())
    driver.add_cookie(
        {'name': '_hjSessionUser_2840334',
         'value': 'eyJpZCI6IjFkMDlhNTJlLTQzZTktNWJlZi1hNzg0LWVhYjk0YzhlNjc1MiIsImNyZWF0ZWQiOjE3MjE0NTYzNDcyMTgsImV4aXN0'
                  'aW5nIjp0cnVlfQ=='})
    sleep(1 + random())


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


def search_field_manager(driver: selenium.webdriver.Chrome, search_inputs: list[str], tag_id: str) -> None:
    """
    Manages the input of search terms into a specified search field and submits the search.

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.
        search_inputs (list[str]): A list of search terms to input.
        tag_id (str): The ID of the search field.
    """
    search_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, tag_id)
        )
    )

    for search_input in search_inputs:
        print(f'Inputting {search_input}...')
        search_field.click()
        sleep(random())
        for char in search_input:
            search_field.send_keys(char)
            sleep(random())
        search_field.send_keys(Keys.RETURN)


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
                                    'n9EIb1D2ANG_5')

    finally:
        print('Shutting Down WebDriver Session...')
        driver.quit()


if __name__ == '__main__':
    main()