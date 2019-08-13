from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://visitcostarica.herokuapp.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    soupStrong = soup.find_all('strong') # soupBook = soup.find_all('div', id_='weather')

    # Get the min avg temp
    min_temp = soupStrong[1].text

    # Get the max avg temp
    max_temp = soupStrong[2].text + 'F'

    # BONUS: Find the src for the sloth image
    # @TODO: YOUR CODE HERE!

    # Store data in a dictionary
    costa_data = {
        "min_temp": min_temp,
        "max_temp": max_temp
    }
#     costa_data = {
#         "sloth_img": sloth_img,
#         "min_temp": min_temp,
#         "max_temp": max_temp
#     }

    # Quit the browser after scraping
    browser.quit()

    # Return results
    return costa_data