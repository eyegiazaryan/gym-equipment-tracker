from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_gym12():
    url = "https://titan.fitness/products/selectorized-leg-extension-and-curl-machine"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Allow JavaScript to load

        try:
            price_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="c-priceMain-template--22413180666133__main"]/div/div/div[1]/span[2]')
                )
            )
            price = price_element.text.strip()
        except:
            print("❌ Price not found")
            price = "Price not available"

        try:
            name_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="c-titleDesktop-template--22413180666133__main"]/p')
                )
            )
            name = name_element.text.strip()
        except:
            print("❌ Product name not found")
            name = "Unknown Product"

        return {
            "name": name,
            "price": price,
            "country": "China",
            "manufacturer": "Titan Fitness",
            "image_url": "https://titan.fitness/cdn/shop/files/401926_01.jpg?v=1739302160&width=832",
            "web_page": url
        }

    finally:
        driver.quit()

if __name__ == "__main__":
    print(scrape_gym12())
