from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_gym4():
    url = "https://shop.straydogstrength.com/products/alpha-half-rack"

    # Extract product details
    name = "Alpha Half Rack"
    price = "$1,750.00"
    country = "USA"
    manufacturer = "Stray Dog Strength"
    image_url = "https://shop.straydogstrength.com/cdn/shop/files/2120-v2-FRAME.jpg?v=1739385447&width=1946"
    web_page = url

    return {"name": name, "price": price, "country": country, "manufacturer": manufacturer, "image_url": image_url, "web_page": web_page}

if __name__ == "__main__":
    scrape_gym4()


