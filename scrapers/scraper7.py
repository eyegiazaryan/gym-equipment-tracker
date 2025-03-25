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

def scrape_gym7():
    url = "https://titan.fitness/products/x-3-series-tall-squat-stand"

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
        sale_status = "regular"

        try:
            # Using provided full XPath for regular price
            price_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='c-priceMain-template--22357952495893__main']/div/div/div[1]/span[2]")
                )
            )
            price = price_element.text.strip()
            logging.info("✅ Regular Price found: %s", price)
        
        except Exception as e:
            logging.warning("❌ Regular price not found. Error: %s", e)

            # Try to get the sale price if regular price is not found
            try:
                sale_price_element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//*[@id='c-priceMain-template--22357952495893__main']/div/div/div[2]/span[4]")
                    )
                )
                price = sale_price_element.text.strip()
                sale_status = "sale"
                logging.info("✅ Sale Price found: %s", price)
            except Exception as e2:
                logging.error("❌ Sale price not found either. Error: %s", e2)

        return {
            "name": "X-3 Series Tall Squat Stand",
            "price": price,
            "status": sale_status,
            "country": "China",
            "manufacturer": "Titan Fitness",
            "image_url": "https://titan.fitness/cdn/shop/files/401403_01_7bfe4696-851b-463e-9c52-7da25209cb6e.jpg?v=1716923804&width=1946",
            "web_page": url
        }

    finally:
        driver.quit()

if __name__ == "__main__":
    product_data = scrape_gym7()
    logging.info("Scraped Data: %s", product_data)
