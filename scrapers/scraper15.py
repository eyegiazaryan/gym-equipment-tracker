from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_gym15():
    url = "https://www.sorinex.com/products/leg-extension-curl-machine?Title=Default+Title"

    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Allow JavaScript to load

        # Extract price
        try:
            price_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'text-xl') and contains(@class, 'font-semibold')]"))
            )
            price = price_element.text.strip()
        except:
            print("❌ Price not found")
            price = "Price not available"

        # Extract product name
        try:
            name_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="relume"]/div/div[2]/h1'))
            )
            name = name_element.text.strip()
        except:
            print("❌ Product name not found")
            name = "Unknown Product"

        return {
            "name": name,
            "price": price,
            "country": "USA",
            "manufacturer": "Sorinex",
            "image_url": "https://cdn.shopify.com/s/files/1/2559/4942/files/LegCurlLegExtension.jpg?v=1733930466",
            "web_page": url
        }

    finally:
        driver.quit()

# Run the scraper
if __name__ == "__main__":
    product_data = scrape_gym15()
    print(product_data)
