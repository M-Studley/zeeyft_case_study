from time import sleep
import bs4
import selenium
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Todo - incorporate google places search

all_countries = ['australia', 'finland', 'canada', 'switzerland', 'japan', ]
query_head = 'wine importers in'
search_engine = 'https://www.google.com'
target_site_name = "Beverage Trade Network"


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


def google_html_parser(driver: selenium.webdriver.Chrome) -> bs4.ResultSet:
    """
    Parses the HTML of the current page loaded in the WebDriver and extracts the search result elements.

    Args:
        driver (selenium.webdriver.Chrome): The WebDriver instance currently in use.

    Returns:
        bs4.ResultSet: A BeautifulSoup ResultSet containing the search result elements.
    """
    page_source = driver.page_source
    tree = BeautifulSoup(page_source, 'html.parser')
    print('Parsing HTML...')
    return tree.find_all('div', class_='g')


def get_url(target: str, result_elements: bs4.ResultSet, country: str) -> dict:
    """
    Searches through the parsed HTML result elements to find the URL of the target site.

    Args:
        target (str): The name of the target site to search for.
        result_elements (bs4.ResultSet): The parsed search result elements.
        country (str): The country being searched.

    Returns:
        dict: A dictionary containing the target site and country as the key, and the found URL as the value.
    """
    modified_target = target.replace(' ', '').lower()
    for result in result_elements:
        url = result.find('a')['href'] if result.find('a') else None
        if modified_target in url:
            return {f'{target} - {country.title()}': url}
    return {}


def query_google(driver: webdriver, url: str, target: str, query: str, country: str) -> dict:
    """
    Performs a Google search for the specified query and country, and extracts the target site URL from the results.

    Args:
        driver (webdriver): The WebDriver instance to perform the search.
        url (str): The base URL of the search engine.
        target (str): The name of the target site to search for.
        query (str): The search query to perform.
        country (str): The country to include in the search query.

    Returns:
        dict: A dictionary containing the target site and country as the key, and the found URL as the value.
    """
    driver.get(url)
    search = driver.find_element(by=By.NAME, value='q')
    search.send_keys(f'{query} {country}')
    search.send_keys(Keys.RETURN)
    print('Awaiting Search Result...')
    sleep(1)
    result_set = google_html_parser(driver)
    url = get_url(target, result_set, country)
    return url


def get_all_country_url(url: str, target: str, query: str, countries: list[str]) -> list[dict]:
    """
    Queries Google for each country in the list and retrieves the target site URLs from the search results.

    Args:
        url (str): The base URL of the search engine.
        target (str): The name of the target site to search for.
        query (str): The search query to perform.
        countries (list[str]): A list of countries to include in the search queries.

    Returns:
        list[dict]: A list of dictionaries containing the target site and country as the key,
        and the found URL as the value.
    """
    all_results = []
    driver = init_chrome_web_driver()
    for country in countries:
        all_results.append(query_google(driver, url, target, query, country))
    print('Shutting Down WebDriver Session...')
    driver.quit()
    return all_results


def main():
    """
    Main function to initiate the Google search scraping process for each country and print the results.
    """
    results = get_all_country_url(search_engine, target_site_name, query_head, all_countries)

    for result in results:
        print(result)


if __name__ == '__main__':
    main()
