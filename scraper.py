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
                                        ElementClickInterceptedException,
                                        NoSuchElementException)
from webdriver_manager.firefox import GeckoDriverManager

ACTIVITY = "Surf"
DEGREE_SYMBOL = "\N{DEGREE SIGN}"
HOME_PAGE_URL = "https://www.metservice.com/marine"
LOCATION = "Lyall Bay"
REGION = "Kapiti and Wellington"


def navigate_to_page(web_driver, selected_region, surf_spot, activity):
    """
    Given the parameters it will navigate through the website to the desired
    webpage

    Parameter:
        web_driver (WebDriver): WebDriver object
        selected_region (str): The region that the surf spot is located
        surf_spot (str): name of the surf location
        activity (str): name of the activity on the webpage

    return: None
    """
    web_driver.get(HOME_PAGE_URL)
    click_page_element(selected_region, "link")
    wait_for_page_title_to_load(selected_region)

    click_page_element(activity, "link")
    click_page_element(surf_spot, "text")
    wait_for_page_title_to_load(f"{surf_spot} Surf Forecast")
    wait_for_page_element_to_be_found("Sea Temperature")  # The title may
    # have loaded correctly. The information on the webpage may not be
    # loaded fully. So this has been added.


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
    print(f"{search} was found")


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
    except (TimeoutException, NoSuchElementException) as ex:
        print(f"Couldn't find {element}. Error was {ex}")
    print(f"{element} was found")
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
    except (TimeoutException, NoSuchElementException) as ex:
        print(f"Couldn't find {element}. Error was {ex}")
    print(f"{element} was found")
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


def get_sea_information(soup_obj):
    """
    This retrieves the "Sea Temperature" information from the webpage. This
    will return the water temperature of the day and the wetsuit
    recommendation for the water

    Parameter:
        soup_obj (BeautifulSoup): BeautifulSoup HTML parsed webpage

    return (tuple): This will return the water temp and wetsuit thickness
                    recommendation
    """
    water_temp = None
    wetsuit_thickness = None
    water_information = soup_obj.findAll("span",
                                         {"class": "u-textBold u-pR-xs"})
    for info in water_information:
        info = info.string
        if DEGREE_SYMBOL in info:
            water_temp = info
        elif "mm" in info:
            wetsuit_thickness = info
    return water_temp, wetsuit_thickness


def get_daily_rating(soup_obj):
    """
    This retrieves the daily overall rating of the surf. This is just a
    value from 1-10, but it tells the rating for the week (including the
    current day)

    Parameter:
        soup_obj (BeautifulSoup): BeautifulSoup HTML parsed webpage

    return (dict): dictionary containing the days and their rating
    """
    daily_rating = soup_obj.findAll("button",
                                    {"class": "Tab-item u-sm-width1of1"})
    daily_surf = {}
    for day in daily_rating:
        button_contents = day.contents
        date = ""
        for count, day_info in enumerate(button_contents):
            detail = day_info.text
            if count == (len(button_contents) - 1):
                day_rating = detail
            else:
                date += detail if detail.isalpha() else f" {detail}"
        daily_surf[date] = {"Overall rating": day_rating}
    return daily_surf


def webscrape_information():
    """
    This navigates to the desired page and then scrapes the desired
    information.

    return: None
    """
    navigate_to_page(driver, REGION, LOCATION, ACTIVITY)

    if LOCATION in driver.title:
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        water_temperature, recommended_wetsuit = get_sea_information(soup)
        print(f"The water temperature today is {water_temperature}. It is "
              f"recommended to use a {recommended_wetsuit} today.")
        surf_week = get_daily_rating(soup)
        print(surf_week)

    else:
        print("Not on the desired webpage")

    driver.quit()  # Quit the instance of the browser that is open


if __name__ == "__main__":
    driver = webdriver.Firefox(
        service=Service(executable_path=GeckoDriverManager().install())
    )
    wait = WebDriverWait(driver, timeout=30)
    webscrape_information()
