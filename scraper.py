# https://www.edureka.co/blog/web-scraping-with-python/#whywebscraping
# https://medium.com/dropout-analytics/selenium-and-geckodriver-on-mac
# -b411dbfe61bc
# The link above was used to learn how to create a web scraper using Python.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

driver_path = '/Users/michaellennonwinton/Downloads/geckodriver'

sea_conditions = []
driver = webdriver.Firefox(executable_path=driver_path)
driver.get("https://www.python.org")

print(driver.title)
