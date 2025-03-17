import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def scrape_gym3():
    url = "https://www.roguefitness.com/rm-3-bolt-together-monster-rack-2-0"

    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        logging.info("Opening website: %s", url)
        driver.get(url)

        # Extract price
        try:
            price_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='main-content']/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/div/div[1]"))
            )
            price = price_element.text.strip()
            logging.info("✅ Price found: %s", price)
        except:
            logging.error("❌ Price not found")
            price = "Price not available"

        # Use the correct image URL (manually set)
        image_url = "https://garagegymlab.com/wp-content/uploads/Rogue-RM-3-Monster-Rack-2.0-Blue.jpg"

        return {
            "name": "Rogue RM-3 Monster Rack 2.0",
            "price": price,
            "country": "USA",
            "manufacturer": "Rogue Fitness",
            "image_url": image_url,
            "web_page": url
        }

    finally:
        driver.quit()

# Run the scraper
if __name__ == "__main__":
    product_data = scrape_gym3()
    logging.info("Scraped Data: %s", product_data)
