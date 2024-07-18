from time import sleep
from random import random

from bs4 import BeautifulSoup
import bs4
import selenium
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

all_countries = ['australia', 'hong kong', 'switzerland', 'poland', 'usa']
query_head = 'wine importers in'
search_engine = 'https://www.google.com'


def init_chrome_web_driver() -> webdriver:
    """
    Initializes a Chrome WebDriver with specific options for headless browsing and language.

    Returns:
        webdriver: Configured Chrome WebDriver instance.
    """
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--language=en")
    driver = webdriver.Chrome(options=options)
    print('Initializing Web Driver...')
    return driver


def xpath_clicker(driver: selenium.webdriver.Chrome) -> None:
    """
    Clicks a specific element on the page using an XPath selector.

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.
    """
    class_name = driver.find_element(By.XPATH, value='//*[@id="hdtb-sc"]/div/div[1]/div[1]/div/div[5]/a') # noqa
    class_name.click()


def scroll_results(driver: selenium.webdriver.Chrome) -> None:
    """
    Scrolls through the search results page until the end of the results is reached.

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
            execute_scroll.send_keys(Keys.END)
            sleep(1 + random())


def google_html_parser(driver: selenium.webdriver.Chrome) -> list[str]:
    """
    Parses the HTML of the current page loaded in the WebDriver and extracts target data.

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.

    Returns:
        list[str]: A list of extracted target data from the search results.
    """
    page_source = driver.page_source
    tree = BeautifulSoup(page_source, 'html.parser')
    print('Parsing HTML...')
    return get_target_data(tree)


def get_target_data(result_elements: bs4.BeautifulSoup) -> list[str]:
    """
    Extracts target data (e.g., company names) from the parsed HTML elements.

    Args:
        result_elements (bs4.BeautifulSoup): Parsed HTML elements.

    Returns:
        list[str]: A list of target data (e.g., company names).
    """
    company_names = []
    tag = result_elements.div
    tags = tag.find_all_next(class_='qBF1Pd fontHeadlineSmall')
    for element in tags:
        company_names.append(element.get_text())
    return company_names


def query_google(driver: webdriver, url: str, query: str, country: str):
    """
    Performs a Google search for the specified query and country, and extracts the target data from the results.

    Args:
        driver (webdriver): The WebDriver instance to perform the search.
        url (str): The base URL of the search engine.
        query (str): The search query to perform.
        country (str): The country to include in the search query.

    Returns:
        list[str]: A list of extracted target data from the search results.
    """
    driver.get(url)
    search = driver.find_element(by=By.NAME, value='q')
    search.click()
    sleep(random())
    search.send_keys(f'{query} {country}')
    sleep(random())
    search.send_keys(Keys.RETURN)
    print('Awaiting Search Result...')
    sleep(1 + random())
    xpath_clicker(driver)
    sleep(1 + random())
    scroll_results(driver)
    result_set = google_html_parser(driver)
    sleep(1 + random())
    return result_set


def get_all_country_url(url: str, query: str, countries: list[str]) -> list[list[str]]:
    """
    Queries Google for each country in the list and retrieves the target data from the search results.

    Args:
        url (str): The base URL of the search engine.
        query (str): The search query to perform.
        countries (list[str]): A list of countries to include in the search queries.

    Returns:
        list[list[str]]: A list of lists containing extracted target data from the search results for each country.
    """
    all_results = []
    for country in countries:
        print(all_results)
        driver = init_chrome_web_driver()
        all_results.append(query_google(driver, url, query, country))
        print('Shutting down WebDriver session...')
        driver.quit()
    return all_results


if __name__ == '__main__':
    results = get_all_country_url(search_engine, query_head, all_countries)
    for result in results:
        print(result)
