# https://www.edureka.co/blog/web-scraping-with-python/#whywebscraping
# https://medium.com/dropout-analytics/selenium-and-geckodriver-on-mac
# -b411dbfe61bc
# The links above was used to learn how to create a web scraper using Python.
from selenium import webdriver
# from bs4 import BeautifulSoup
# import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common.exceptions import TimeoutException

driver_path = '/Users/michaellennonwinton/Downloads/geckodriver'


def wait_for_page_to_load(search):
    print(f"Searching for {search}")
    try:
        element_present = Ec.title_contains(search)
        wait.until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")


def wait_for_page_element(element):
    print(f"Waiting for {element} to be present")
    try:
        element_present = Ec.element_to_be_clickable((By.LINK_TEXT, element))
        wait.until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")


driver = webdriver.Firefox(executable_path=driver_path)
driver.get("https://www.metservice.com/marine")
wait = WebDriverWait(driver, timeout=30, poll_frequency=2)
webpage = driver.page_source
area = driver.find_element(by=By.LINK_TEXT, value="Kapiti and Wellington")
area.click()
wait_for_page_to_load("Kapiti and Wellington")
surf = (driver.find_element(by=By.LINK_TEXT, value="Surf"))
surf.click()
wait_for_page_to_load("Surf")

bay = driver.find_element(by=By.XPATH, value="//div[@title='Lyall Bay']")
bay.click()

wait_for_page_element("View full surf forecasts")
location_forecast = (driver.find_element(by=By.LINK_TEXT,
                                         value="View full surf forecasts"))
location_forecast.click()
