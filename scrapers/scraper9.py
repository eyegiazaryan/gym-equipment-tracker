def scrape_gym9():
    """Scraper for Stray Dog - No Squat Stand Available"""
    return {
        "name": "No Squat Stand Available",
        "price": "NA",  # No price available
        "country": "USA",
        "manufacturer": "Stray Dog Strength",
        "image_url": "https://t3.ftcdn.net/jpg/01/12/43/90/360_F_112439022_Sft6cXK9GLnzWjjIkVMj2Lt34RcKUpxm.jpg",
        "web_page": "NA"  # No valid product page
    }

# Run the scraper
if __name__ == "__main__":
    product_data = scrape_gym9()
    print(product_data)
