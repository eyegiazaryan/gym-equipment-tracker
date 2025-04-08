import logging

def scrape_gym11():
    """Scraper for Oak Club MFG - No Leg Extension Available"""

    logging.warning("⚠️ Oak Club MFG does not have a leg extension available.")

    return {
        "name": "No Leg Extension Available",
        "price": "Not Available",
        "country": "Canada",
        "manufacturer": "Oak Club MFG",
        "image_url": "https://t3.ftcdn.net/jpg/01/12/43/90/360_F_112439022_Sft6cXK9GLnzWjjIkVMj2Lt34RcKUpxm.jpg",
        "web_page": "Not Available"
    }

if __name__ == "__main__":
    print(scrape_gym11())
