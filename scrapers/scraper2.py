import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def scrape_gym2():
    url = "https://titan.fitness/products/titan-series-power-rack-90-36?variant=47930285916437"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        logging.info("Opening website: %s", url)
        driver.get(url)
        time.sleep(5)  # Allow JavaScript content to fully load

        price = "Price not available"

        try:
            # Using the provided full XPath
            regular_price_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="c-priceMain-template--22357952495893__main"]/div/div/div[2]/span[2]')
                )
            )
            price = regular_price_element.text.strip()
            logging.info("✅ Regular Price found: %s", price)

        except Exception as e:
            logging.error("❌ Regular price not found. Error: %s", e)
            price = "Not available"

        return {
            "name": 'TITAN Series Power Rack 90" 36"',
            "price": price,
            "country": "China",
            "manufacturer": "Titan Fitness",
            "image_url": "https://titan.fitness/cdn/shop/files/401223_01.jpg?v=1722443777&width=1946",
            "web_page": url
        }

    finally:
        driver.quit()

if __name__ == "__main__":
    product_data = scrape_gym2()
    logging.info("Scraped Data: %s", product_data)
