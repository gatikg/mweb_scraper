import time
from selenium import webdriver
from web_driver import web_driver
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs

def scrape_google_top_stories_selenium(query):
    driver = web_driver()

    query = quote_plus(query)
    url = f"https://www.google.com/search?q={query}&gl=in"

    driver.get(url)
    time.sleep(3)

    soup = bs(driver.page_source, 'html.parser')
    driver.quit()
    return soup