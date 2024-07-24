import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def copy_email(driver: selenium.webdriver.Chrome) -> None:
    email = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#copy_address')
        )
    )
    email.click()


def click_email(driver: selenium.webdriver.Chrome) -> None:
    email = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#mail_messages_content > div')
        )
    )
    email.click()


def email_body(driver: selenium.webdriver.Chrome) -> None:
    body = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(
            (By.XPATH,
             '//*[@class="message_bottom"]/div[6]')
        )
    )
