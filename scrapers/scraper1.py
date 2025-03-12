from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_gym1():
    url = "https://oakclubmfg.com/collections/corporate-racks/products/the-corporate-rack"

    name = "The Corporate Rack"
    price = "$2,049.00"
    country = "Canada"
    manufacturer = "Oak Club MFG"
    image_url = "https://oakclubmfg.com/cdn/shop/products/210123_stockracks_8144_1800x1800.jpg?v=1617242493"
    web_page = url

    return {"name": name, "price": price, "country": country, "manufacturer": manufacturer, "image_url": image_url, "web_page": web_page}

if __name__ == "__main__":
    scrape_gym1()

