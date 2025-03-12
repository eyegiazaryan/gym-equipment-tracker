def scrape_gym8():
    url = "https://www.sorinex.com/products/xl-half-rack?Attachment+Color=Black+Texture&Upgrades=None"

    # Extract product details
    name = "XL™ Series Half Rack"
    price = "$2,399.00"
    country = "USA"
    manufacturer = "Sorinex"
    image_url = "https://cdn.shopify.com/s/files/1/2559/4942/products/XL_HalfRack_BlackTexture.jpg?v=1539894443"  
    web_page = url

    return {
        "name": name,
        "price": price,
        "country": country,
        "manufacturer": manufacturer,
        "image_url": image_url,
        "web_page": web_page
    }
