from time import sleep
import bs4
import selenium
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Todo - make all functions universal
# Todo - document all functions

all_countries = ['australia', 'finland', 'canada', 'switzerland', 'japan', ]
query_head = 'wine importers in'
link = 'https://www.google.com'
target_site_name = "Beverage Trade Network"


def init_chrome_web_driver() -> webdriver:
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--language=en")
    driver = webdriver.Chrome(options=options)
    print('Initializing Web Driver...')
    return driver


def google_html_parser(driver: selenium.webdriver.Chrome) -> bs4.ResultSet:
    page_source = driver.page_source
    tree = BeautifulSoup(page_source, 'html.parser')
    print('Parsing HTML...')
    return tree.find_all('div', class_='g')


def get_url(target: str, result_elements: bs4.ResultSet, country: str) -> dict:
    modified_target = target.replace(' ', '').lower()
    for result in result_elements:
        url = result.find('a')['href'] if result.find('a') else None
        if modified_target in url:
            return {f'{target} - {country.title()}': url}
    return {}


def query_google(driver: webdriver, url: str, target: str, query: str, country: str) -> dict:
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
    all_results = []
    driver = init_chrome_web_driver()
    for country in countries:
        all_results.append(query_google(driver, url, target, query, country))
    print('Shutting Down Web Driver Session...')
    driver.quit()
    return all_results


results = get_all_country_url(link, target_site_name, query_head, all_countries)

for result in results:
    print(result)
