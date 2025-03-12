from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape_gym3():
    url = "https://www.roguefitness.com/rm-3-bolt-together-monster-rack-2-0"

    # Extract product details
    name = "Rogue RM-3 Monster Rack 2.0"
    price = "$1,520.00"
    country = "USA"
    manufacturer = "Rogue Fitness"
    image_url = "https://tokofitness.id/wp-content/uploads/2019/05/download-500x671.png"
    web_page = url

    return {"name": name, "price": price, "country": country, "manufacturer": manufacturer, "image_url": image_url, "web_page": web_page}

if __name__ == "__main__":
    scrape_gym3()


