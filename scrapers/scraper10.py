from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_gym10():
    url = "https://www.roguefitness.com/rogue-sm-2-5-monster-squat-stand-2-0"

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
                EC.presence_of_element_located((By.XPATH, "//*[@id='pdp-rhpa']/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/div[1]"))
            )
            price = price_element.text.strip()
        except:
            print("❌ Price not found")
            price = "Price not available"

        return {
            "name": "Rogue SM-2.5 Monster Squat Stand 2.0",
            "price": price,
            "country": "USA",
            "manufacturer": "Rogue Fitness",
            "image_url": "https://assets.roguefitness.com/f_auto,q_auto,c_limit,w_1042,b_rgb:f8f8f8/catalog/Rigs%20and%20Racks/Squat%20Stands/S2SQUAT2-0/S2SQUAT2-0-H_bmnpsa.png",
            "web_page": url
        }

    finally:
        driver.quit()

# Run the scraper
if __name__ == "__main__":
    product_data = scrape_gym10()
    print(product_data)
