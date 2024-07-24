from time import sleep
from random import randint
from dataclasses import dataclass

import selenium
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


def init_chrome_web_driver(headless: bool = False,
                           maximized: bool = True) -> webdriver:
    """
    Initializes a Chrome WebDriver with specific options for headless and maximized window.

    :param headless: Default = False
    :param maximized: Default = True

    :return webdriver.Chrome: Configured Chrome WebDriver instance.
    """
    options = ChromeOptions()
    if headless is True:
        options.add_argument("--headless=new")

    if maximized is True:
        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    print('Initializing WebDriver...')

    return driver


def navigate_target_url(driver: selenium.webdriver.Chrome,
                        target_url: str,
                        sleep_time_seconds: int = 0) -> None:
    """
    Navigates the WebDriver to the target URL.

    :param sleep_time_seconds: Amount of seconds to sleep.
    :param driver: The WebDriver instance currently in use.
    :param target_url: Desired URL to navigate to.
    """
    print(f'Navigating to {target_url}')
    driver.get(target_url)
    sleep(sleep_time_seconds)

    if sleep_time_seconds != 0:
        print(f'Sleeping {sleep_time_seconds} seconds...')


def cookie_manager(driver: selenium.webdriver.Chrome, cookies: list[dict]) -> None:
    """
    Adds predefined cookies to the WebDriver session to manage authentication or session state.

    :param driver: (selenium.webdriver.Chrome)
    :param cookies: list[dict]
    """
    for cookie in cookies:
        print(f'Adding Cookie...\n{cookie}')
        driver.add_cookie(
            cookie
        )


def random_email_generator(domain: str) -> str:
    """
    Generates a random email address for testing purposes.

    :param domain: (str) email domain suffix

    :returns str: A randomly generated email address.
    """
    random_email = ''
    for i in range(14 + 1):
        random_email += chr(randint(97, 122))

    print('Generating random email...')
    return f'{random_email}@{domain}'


def random_password_generator(password_length: int) -> str:
    """
    Generates a random email address for testing purposes.
    Currently, not in use.

    :param password_length: (int) length of password desired

    :returns str: A randomly generated email address.
    """
    random_password = ''
    for i in range(password_length + 1):
        random_password += chr(randint(48, 122))

    print('Generating Random Password...')
    return random_password


def scroll_by_delta_x_and_y(driver: selenium.webdriver.Chrome, delta_x: int, delta_y: int) -> None:
    """
    Performs scrolling on the page by coordinates.

    :param driver: (selenium.webdriver.Chrome)
    :param delta_x: (int) horizontal
    :param delta_y: (int) vertical

    :return: None
    """
    print(f'Scrolling to coord: {delta_x},{delta_y}')
    ActionChains(driver) \
        .scroll_by_amount(delta_x, delta_y) \
        .perform()


def execute_with_error_handling(func, *args, **kwargs) -> None:
    """
    Executes a given function with error handling for NoSuchElementException.
    WARNING! This is NOT for using when needing a return value! (.text, .get_attribute, etc.)

    :param func: (callable) The function to execute.
    :param args: Positional arguments to pass to the function.
    :param kwargs: Keyword arguments to pass to the function.
    """
    try:
        return func(*args, **kwargs)
    except NoSuchElementException as e:
        print(f'{func.__name__} Failed! Exception: {str(e)}')


@dataclass
class Pagination:

    @staticmethod
    def fetch_total_pages(*, driver: selenium.webdriver.Chrome,
                          coord: tuple,
                          css_selector: WebElement) -> int:
        scroll_by_delta_x_and_y(driver=driver,
                                delta_x=coord[0],
                                delta_y=coord[1])

        page_total = driver.find_element(
            By.CSS_SELECTOR,
            value=f'{css_selector}').text

        return int(page_total)

    @staticmethod
    def click_next_page_button(*, driver: selenium.webdriver.Chrome,
                               coord: tuple,
                               css_selector: WebElement) -> None:
        scroll_by_delta_x_and_y(driver=driver,
                                delta_x=coord[0],
                                delta_y=coord[1])

        locate_next_page = driver.find_element(
            By.CSS_SELECTOR,
            value=f'{css_selector}')

        next_page_btn = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable(locate_next_page))

        next_page_btn.click()
