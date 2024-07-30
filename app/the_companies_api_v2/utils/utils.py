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


def init_chrome_web_driver(headless: bool = False,
                           maximized: bool = True) -> webdriver.Chrome:
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


def navigate_target_url(*, driver: selenium.webdriver.Chrome,
                        target_url: str,
                        sleep_sec: int = 0) -> None:
    """
    Navigates the WebDriver to the target URL.

    :param sleep_sec: Amount of seconds to sleep.
    :param driver: The WebDriver instance currently in use.
    :param target_url: Desired URL to navigate to.
    """
    print(f'Navigating to {target_url}')
    driver.get(target_url)
    sleep(sleep_sec)

    if sleep_sec != 0:
        print(f'Sleeping {sleep_sec} seconds...')


def cookie_manager(*, driver: selenium.webdriver.Chrome,
                   cookies: list[dict]) -> None:
    """
    Adds predefined cookies to the WebDriver session to manage authentication or session state.

    :param driver: (selenium.webdriver.Chrome)
    :param cookies: list[dict]
    """
    for cookie in cookies:
        print(f'Adding Cookie...\n{cookie}')
        driver.add_cookie(cookie)


def random_email_generator(*, domain: str) -> str:
    """
    Generates a random email address for testing purposes.

    :param domain: (str) email domain suffix

    :return str: A randomly generated email address.
    """
    random_email = ''
    for i in range(14 + 1):
        random_email += chr(randint(97, 122))

    print('Generating random email...')
    return f'{random_email}@{domain}'


def random_password_generator(*, password_length: int) -> str:
    """
    Generates a random email address for testing purposes.
    Currently, not in use.

    :param password_length: (int) length of password desired

    :return str: A randomly generated email address.
    """
    random_password = ''
    for i in range(password_length + 1):
        random_password += chr(randint(48, 122))

    print('Generating Random Password...')
    return random_password


def scroll_by_delta_x_and_y(*, driver: selenium.webdriver.Chrome,
                            coord: tuple[int, int]) -> None:
    """
    Performs scrolling on the page by coordinates.

    :param driver: (selenium.webdriver.Chrome)
    :param coord: (tuple[int, int]) tuple[0] = x, tuple[1] = y

    :return: None
    """
    print(f'Scrolling to coord: {coord[0]},{coord[1]}')
    ActionChains(driver) \
        .scroll_by_amount(coord[0], coord[1]) \
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
                          coord: tuple[int, int],
                          css_selector: str) -> int:

        scroll_by_delta_x_and_y(driver=driver,
                                coord=coord)

        page_total = driver.find_element(
            By.CSS_SELECTOR,
            value=f'{css_selector}').text

        return int(page_total)

    @staticmethod
    def click_next_page_button(*, driver: selenium.webdriver.Chrome,
                               coord: tuple[int, int],
                               css_selector: str) -> None:
        scroll_by_delta_x_and_y(driver=driver,
                                coord=coord)

        locate_next_page = driver.find_element(
            By.CSS_SELECTOR,
            value=css_selector)

        next_page_btn = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable(locate_next_page))

        next_page_btn.click()


@dataclass
class WindowManager:

    @staticmethod
    def open_new_window(*, driver: selenium.webdriver.Chrome, target_url: str, sleep_sec: int = 0) -> list[str]:
        print("Getting Primary Window Handle...")
        primary_window = driver.current_window_handle

        print("Opening New Window")
        driver.switch_to.new_window('window')

        print("Getting Secondary Window Handle...")
        secondary_window = driver.current_window_handle

        navigate_target_url(driver=driver, target_url=target_url, sleep_sec=sleep_sec)

        return [primary_window, secondary_window]

    @staticmethod
    def close_new_window(*, driver: selenium.webdriver.Chrome, handles: list[str]) -> None:

        driver.switch_to.window(handles[-1])

        driver.close()

        driver.switch_to.window(handles[0])