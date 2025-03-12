def scrape_gym7():
    url = "https://titan.fitness/products/x-3-series-tall-squat-stand"

    # Extract product details
    name = "X-3 Series Tall Squat Stand"
    price = "$459.99"
    country = "China"
    manufacturer = "Titan Fitness"
    image_url = "https://titan.fitness/cdn/shop/files/401403_01_7bfe4696-851b-463e-9c52-7da25209cb6e.jpg?v=1716923804&width=1946" 
    web_page = url

    return {
        "name": name,
        "price": price,
        "country": country,
        "manufacturer": manufacturer,
        "image_url": image_url,
        "web_page": web_page
    }
