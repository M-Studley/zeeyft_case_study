from time import sleep
from random import random

import selenium
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

all_countries = ['australia', 'hong kong', 'switzerland', 'poland', 'usa']
query_head = 'wine importers in'
search_engine = 'https://www.google.com/maps/search/wine+importers+in+'


# def language_selector_head_only(driver: selenium.webdriver.Chrome):
#     """
#     A convoluted solution to translating a page to the English language
#     """
#     import pyautogui
#     from selenium.webdriver import ActionChains
#     action = ActionChains(driver)
#     left_pane_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[2]/div[3]'
#     left_pane = driver.find_element(By.XPATH, value=left_pane_xpath)
#     action.context_click(left_pane).perform()
#     sleep(1 + random())
#     for i in range(1, 8 + 1):
#         pyautogui.press('down')
#     sleep(1)
#     pyautogui.press('enter')


def init_chrome_web_driver() -> webdriver:
    """
    Initializes a Chrome WebDriver with specific options for language, headless, and maximized window.

    Returns:
        webdriver.Chrome: Configured Chrome WebDriver instance.
    """
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--lang=en-US")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    print('Initializing WebDriver...')
    return driver


def scroll_results_window(driver: selenium.webdriver.Chrome) -> None:
    """
    Scrolls through the search results page until the end of the results is reached by using scroll and page down keys.

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.
    """
    left_pane_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]'
    driver.find_element(By.XPATH, value=left_pane_xpath).click()
    execute_scroll = driver.find_element(By.XPATH, value=left_pane_xpath)
    while True:
        try:
            end_of_results = driver.find_element(By.CLASS_NAME, value='HlvSq')
            if end_of_results:
                break
        except NoSuchElementException:
            pass
        finally:
            execute_scroll.send_keys(Keys.END)
            sleep(1 + random())
            execute_scroll.send_keys(Keys.PAGE_DOWN)
            sleep(2 + random())
            print('Scrolling Result Window...')


def get_target_data(driver: selenium.webdriver.Chrome) -> list[dict[str, str]]:
    """
    Extracts target data (e.g., company names) from the parsed HTML elements.

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.

    Returns:
        list[str]: A list of target data (e.g., company names).
    """

    elements = driver.find_elements(By.CSS_SELECTOR, value='div[role="feed"] > div > div[jsaction]')

    results = []
    for element in elements:
        target_data = {}

        try:
            target_data['title'] = element.find_element(By.CSS_SELECTOR, value='.fontHeadlineSmall').text
        except Exception:
            target_data['title'] = 'None'

        try:
            target_data['url'] = element.find_element(By.CSS_SELECTOR, value='a.lcr4fd.S9kvJb').get_attribute('href')
        except Exception:
            target_data['url'] = 'None'

        try:
            target_data['phone'] = element.find_element(By.CLASS_NAME, value='UsdlK').text
        except Exception:
            target_data['phone'] = 'None'

        try:
            target_data['address'] = element.find_element(
                By.CSS_SELECTOR,
                value='div[role="feed"] .fontBodyMedium > div:nth-child(4) > '
                      'div > span:nth-child(2) > span:nth-child(2)').text
        except Exception:
            target_data['address'] = 'None'

        if target_data.get('title') != 'None':
            results.append(target_data)

    return results


def query_google(driver: webdriver, url: str):
    """
    Performs a Google search for the specified URL and extracts the target data from the results.

    Args:
        driver (webdriver.Chrome): The WebDriver instance to perform the search.
        url (str): The URL to search.

    Returns:
        list[str]: A list of extracted target data from the search results.
    """
    driver.get(url)
    sleep(1 + random())
    scroll_results_window(driver)
    sleep(10 + random())
    sleep(1 + random())
    return get_target_data(driver)


def get_all_country_url(url: str, countries: list[str]) -> list[list[str]]:
    """
    Queries Google for each country in the list and retrieves the target data from the search results.

    Args:
        url (str): The base URL of the search engine.
        countries (list[str]): A list of countries to include in the search queries.

    Returns:
        list[list[str]]: A list of lists containing extracted target data from the search results for each country.
    """
    try:
        all_results = []
        driver = init_chrome_web_driver()
        for country in countries:
            modified_url = url + country
            all_results.append(query_google(driver, modified_url))
    finally:
        print('Shutting down WebDriver session...')
        driver.quit()

    return all_results


if __name__ == '__main__':
    all_results = get_all_country_url(search_engine, countries=['australia'])
    for result in all_results:
        print(result)
