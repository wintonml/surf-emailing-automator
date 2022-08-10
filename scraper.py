"""
This program will scrape the data from a surf forecast website.

https://www.edureka.co/blog/web-scraping-with-python/#whywebscraping
https://medium.com/dropout-analytics/selenium-and-geckodriver-on-mac
-b411dbfe61bc
The links above was used to learn how to create a web scraper using Python.
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (TimeoutException,
                                        ElementClickInterceptedException)
from webdriver_manager.firefox import GeckoDriverManager


def wait_for_page_title_to_load(search):
    """
    This waits for the webpage to load by waiting for the webpage's title to
    present.

    Parameter:
        search (str): string that is being searched for

    return: None
    """
    print(f"Searching for {search}")
    try:
        element_present = ec.title_contains(search)
        wait.until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")


def wait_for_clickable_page_element(element):
    """
    This waits for the webpage to load by waiting for an element on the
    webpage to be clickable.

    Parameter:
        element (str): string that is being searched for

    return:
    """
    print(f"Waiting for {element} to be present")
    try:
        element_present = ec.element_to_be_clickable((By.LINK_TEXT, element))
        clickable_element = wait.until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    return clickable_element


def wait_for_page_element_to_be_found(element):
    """
    This waits for the webpage to load by waiting for an element text to be
    present.

    Parameter:
        element (str): string that is being searched for

    return:
    """
    print(f"Waiting for {element} to be present")
    try:
        element_present = ec.text_to_be_present_in_element(
            (By.XPATH, f'//*[contains(text(), "{element}")]'), element)
        wait.until(element_present)
    except TimeoutException:
        print(f"Timed out waiting for page to load. Couldn't find {element}")
    return driver.find_element(By.XPATH, f"//*[contains(text(), '{element}')]")


def click_page_element(element, element_type):
    """
    This will wait for the page element that will be clicked to load and
    then click the text/link.

    Parameter:
        element (str): string that is being searched for
        element_type (str): the type of the element being searched for i.e.
            link, text, id, etc.

    return:
    """

    try:
        if element_type == "link":
            web_element = wait_for_clickable_page_element(element)
        elif element_type == "text":
            web_element = wait_for_page_element_to_be_found(element)
        web_element.click()
    except ElementClickInterceptedException:
        print(f"Couldn't find: {element}. Trying to click on the button "
              f"again")
        driver.execute_script("arguments[0].click()", web_element)


driver = webdriver.Firefox(
    service=Service(executable_path=GeckoDriverManager().install())
)
driver.get("https://www.metservice.com/marine")
wait = WebDriverWait(driver, timeout=30)
webpage = driver.page_source
area = driver.find_element(by=By.LINK_TEXT, value="Kapiti and Wellington")
area.click()
wait_for_page_title_to_load("Kapiti and Wellington")

click_page_element("Surf", "link")
click_page_element("Lyall Bay", "text")

wait_for_page_element_to_be_found("Sea Temperature")

get_title = driver.title
print(get_title)

if "Lyall Bay" in get_title:

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    print(soup.prettify())
else:
    print("Page did not load correctly")

driver.quit()
