# https://www.edureka.co/blog/web-scraping-with-python/#whywebscraping
# The link above was used to learn how to create a web scraper using Python.

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.safari()

sea_conditions = []
driver.get("https://www.metservice.com/marine/regions/kapiti-wellington/surf"
           "/locations/lyall-bay")
