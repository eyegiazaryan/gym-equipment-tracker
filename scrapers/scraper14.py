from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_gym14():
    url = "https://shop.straydogstrength.com/products/selectorized-seated-leg-curl-extension"

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
                EC.presence_of_element_located((By.XPATH, "//*[@id='price-template--17914059948282__main']/div/div/div[1]/span[2]"))
            )
            price = price_element.text.strip()
            price = price.replace("USD", "").replace("$", "").strip()
            price = f"${price}"
        except Exception as e:
            print(f"❌ Price not found: {e}")
            price = "Price not available"

        # Extract product name
        try:
            name_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='ProductInfo-template--17914059948282__main']/div[1]/h1"))
            )
            name = name_element.text.strip()
        except Exception as e:
            print(f"❌ Name not found: {e}")
            name = "Unknown Product"

        return {
            "name": name,
            "price": price,
            "country": "USA",
            "manufacturer": "Stray Dog Strength",
            "image_url": "https://shop.straydogstrength.com/cdn/shop/files/2325-RIGHT-RED_eee5d4da-9504-4bb9-b7e3-f98e7e85c231.jpg?v=1743705611&width=823",
            "web_page": url
        }

    finally:
        driver.quit()

# Run the scraper
if __name__ == "__main__":
    product_data = scrape_gym14()
    print(product_data)
