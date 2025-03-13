from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_gym2():
    url = "https://titan.fitness/products/titan-series-power-rack-90-36?variant=47930285916437"

    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Allow JavaScript to load

        # Extract Regular Price
        try:
            regular_price_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='c-priceMain-template--22327592452373__main']/div/div/div[2]/span[2]"))
            )
            regular_price = regular_price_element.text.strip()
        except:
            print("❌ Regular price not found")
            regular_price = "Not available"

        # Extract Sale Price
        try:
            sale_price_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='c-priceMain-template--22327592452373__main']/div/div/div[2]/span[4]"))
            )
            sale_price = sale_price_element.text.strip()
        except:
            sale_price = None  # If no sale price is available

        # Set the current price (use sale price if available, otherwise use regular price)
        price = sale_price if sale_price else regular_price

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

# Run the scraper
if __name__ == "__main__":
    product_data = scrape_gym2()
    print(product_data)
