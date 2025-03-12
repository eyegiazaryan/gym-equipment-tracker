def scrape_gym10():
    url = "https://www.roguefitness.com/rogue-sm-2-5-monster-squat-stand-2-0"

    # Extract product details
    name = "Rogue SM-2.5 Monster Squat Stand 2.0"
    price = "$820.00"
    country = "USA"
    manufacturer = "Rogue Fitness"
    image_url = "https://assets.roguefitness.com/f_auto,q_auto,c_limit,w_1042,b_rgb:f8f8f8/catalog/Rigs%20and%20Racks/Squat%20Stands/S2SQUAT2-0/S2SQUAT2-0-H_bmnpsa.png"  # **Updated Image URL**
    web_page = url

    return {
        "name": name,
        "price": price,
        "country": country,
        "manufacturer": manufacturer,
        "image_url": image_url,  # **Correct external image URL**
        "web_page": web_page  # **Ensure the correct website is linked**
    }
