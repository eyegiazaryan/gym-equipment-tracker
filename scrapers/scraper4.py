from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_gym4():
    url = "https://shop.straydogstrength.com/products/alpha-half-rack"

    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Allow JavaScript to load

        # Extract price using the correct XPath
        try:
            price_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='price-template--17914059948282__main']/div/div/div[1]/span[2]"))
            )
            price = price_element.text.strip()

            # Remove 'USD' and '$' from the price if it exists
            price = price.replace("USD", "").replace("$", "").strip()

        except Exception as e:
            print(f"❌ Price not found: {e}")
            price = "Price not available"

        return {
            "name": "Alpha Half Rack",
            "price": price,
            "country": "USA",
            "manufacturer": "Stray Dog Strength",
            "image_url": "https://shop.straydogstrength.com/cdn/shop/files/2120-v2-FRAME.jpg?v=1739385447&width=1946",
            "web_page": url
        }

    finally:
        driver.quit()

# Run the scraper
if __name__ == "__main__":
    product_data = scrape_gym4()
    print(product_data)
