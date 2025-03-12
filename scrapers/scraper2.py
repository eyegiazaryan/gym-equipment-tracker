from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_gym2():
    url = "https://titan.fitness/products/titan-series-power-rack-90-36?variant=47930285916437"

    name = 'TITAN Series Power Rack 90" 36"'
    price = "$859.97"
    country = "China"
    manufacturer = "Titan Fitness"
    image_url = "https://titan.fitness/cdn/shop/files/401223_01.jpg?v=1722443777&width=1946"
    web_page = url

    return {"name": name, "price": price, "country": country, "manufacturer": manufacturer, "image_url": image_url, "web_page": web_page}

if __name__ == "__main__":
    scrape_gym2()
