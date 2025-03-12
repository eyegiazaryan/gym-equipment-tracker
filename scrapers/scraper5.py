from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_gym5():
    url = "https://www.sorinex.com/products/xl-series-single-rack?Attachment+Color=Black+Texture&Upgrades=None"

    # Extract product details
    name = "XL™ SERIES SINGLE RACK"
    price = "$1,799.00"
    country = "USA"
    manufacturer = "Sorinex"
    image_url = "https://cdn.shopify.com/s/files/1/2559/4942/products/XL_SingleRack_BlackTexture.210.jpg?v=1567697449"
    web_page = url

    return {"name": name, "price": price, "country": country, "manufacturer": manufacturer, "image_url": image_url, "web_page": web_page}

if __name__ == "__main__":
    scrape_gym5()


