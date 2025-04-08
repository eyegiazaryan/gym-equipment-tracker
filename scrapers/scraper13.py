import logging

def scrape_gym13():
    """Scraper for Rogue Fitness - No Leg Extension Available"""

    logging.warning("⚠️ Rogue Fitness does not have a leg extension available.")

    return {
        "name": "No Leg Extension Available",
        "price": "Not Available",
        "country": "USA",
        "manufacturer": "Rogue Fitness",
        "image_url": "https://t3.ftcdn.net/jpg/01/12/43/90/360_F_112439022_Sft6cXK9GLnzWjjIkVMj2Lt34RcKUpxm.jpg",
        "web_page": "Not Available"
    }

if __name__ == "__main__":
    print(scrape_gym13())
