import requests
from bs4 import BeautifulSoup

# Header to become udetectable
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}


def create_url(product_name):
    """
    Generate an Amazon search URL for a given product name.

    This function takes a product name, formats it by replacing spaces with 
    plus signs (`+`) to match Amazon's search URL structure, and returns the
    complete search URL.

    Args:
        product_name (str): The name of the product to search for on Amazon.

    Returns:
        str: A formatted Amazon search URL.

    Example:
        >>> create_url("coffee grinder")
        'https://www.amazon.com/s?k=coffee+grinder'

        >>> create_url("sleek black laptop stand")
        'https://www.amazon.com/s?k=sleek+black+laptop+stand'
    """
    base_url = "https://www.amazon.com/s?k="

    # Replace spaces with plus signs
    formatted_product_name = product_name.replace(" ", "+")
    search_url = f"{base_url}{formatted_product_name}"
    return search_url


def extract_product_data(soup):
    """
    Extract product data from an Amazon search results page.

    This function parses the provided BeautifulSoup object to extract information
    about products displayed on the Amazon search results page. It collects
    the title, rating, and price of each product and stores the data in a list of dictionaries.

    Args:
        soup (BeautifulSoup): A BeautifulSoup object representing the HTML content of the Amazon search results page.

    Returns:
        list[dict]: A list of dictionaries where each dictionary contains the following keys:
            - "title" (str): The product's title or "N/A" if unavailable.
            - "rating" (str): The product's rating or "N/A" if unavailable.
            - "price" (str): The product's price or "N/A" if unavailable.

    Example:
        >>> soup = BeautifulSoup(html_content, "html.parser")
        >>> products = extract_product_data(soup)
        >>> print(products)
        [
            {"title": "Sleek Black Coffee Grinder", "rating": "4.5 out of 5 stars", "price": "$49.99"},
            {"title": "Compact Coffee Grinder", "rating": "4.3 out of 5 stars", "price": "$39.99"},
        ]
    """
    products = []
    # Locate all product containers
    product_containers = soup.find_all(
        "div", class_="a-section a-spacing-small puis-padding-left-small puis-padding-right-small")
    for container in product_containers:
        product_data = {}

        # Extract the title
        title_section = container.find("div", {"data-cy": "title-recipe"})
        if title_section:
            link = title_section.find(
                "a", class_="a-link-normal s-line-clamp-4 s-link-style a-text-normal")
            if link:
                title = link.find("span")
                if title:
                    product_data["title"] = title.text.strip()

        # Extract the reviews
        reviews_section = container.find("div", {"data-cy": "reviews-block"})
        if reviews_section:
            rating = reviews_section.find("span", class_="a-icon-alt")
            product_data["rating"] = rating.text.strip() if rating else "N/A"

        # Extract the price
        price_section = container.find("div", {"data-cy": "price-recipe"})
        if price_section:
            price = price_section.find("span", class_="a-offscreen")
            product_data["price"] = price.text.strip() if price else "N/A"

        products.append(product_data)

    return products


# Extract product data
def extract_product_info(productName):
    """
    Extract product information by scraping Amazon's search results page.

    This function takes a product name, constructs the corresponding Amazon search URL,
    sends a GET request to retrieve the HTML content, and parses the content to extract
    product data.

    Args:
        productName (str): The name of the product to search for on Amazon.

    Returns:
        list[dict]: A list of dictionaries containing product data, including title, rating, and price.

    Example:
        >>> products = extract_product_info("coffee grinder")
        >>> print(products)
        [
            {"title": "Sleek Black Coffee Grinder", "rating": "4.5 out of 5 stars", "price": "$49.99"},
            {"title": "Compact Coffee Grinder", "rating": "4.3 out of 5 stars", "price": "$39.99"},
        ]
    """
    response = requests.get(create_url(productName), headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    return extract_product_data(soup)


def seperate_product_info(products):
    """
    Separate product information into individual lists.

    This function processes a list of product dictionaries and separates their
    data into three lists: titles, ratings, and prices.

    Args:
        products (list[dict]): A list of dictionaries, where each dictionary contains
                            product information such as title, rating, and price.

    Returns:
        tuple: A tuple containing three lists:
            - titles (list[str]): A list of product titles.
            - ratings (list[str]): A list of product ratings.
            - prices (list[str]): A list of product prices.

    Example:
        >>> products = [
                {"title": "Sleek Black Coffee Grinder", "rating": "4.5 out of 5 stars", "price": "$49.99"},
                {"title": "Compact Coffee Grinder", "rating": "4.3 out of 5 stars", "price": "$39.99"},
            ]
        >>> titles, ratings, prices = seperate_product_info(products)
        >>> print(titles)
        ['Sleek Black Coffee Grinder', 'Compact Coffee Grinder']
    """
    titles = []
    ratings = []
    prices = []
    for product in products:
        titles.append(product.get('title'))
        ratings.append(product.get('rating'))
        prices.append(product.get('price'))

    return titles, ratings, prices

# Print the results


def print_product_info(products):
    """
    Print product information in a human-readable format.

    This function takes a list of product dictionaries and prints the title,
    rating, and price of each product in a formatted way.

    Args:
        products (list[dict]): A list of dictionaries, where each dictionary contains
                            product information such as title, rating, and price.

    Returns:
        None

    Example:
        >>> products = [
                {"title": "Sleek Black Coffee Grinder", "rating": "4.5 out of 5 stars", "price": "$49.99"},
                {"title": "Compact Coffee Grinder", "rating": "4.3 out of 5 stars", "price": "$39.99"},
            ]
        >>> print_product_info(products)
        Product 1:
        Title: Sleek Black Coffee Grinder
        Rating: 4.5 out of 5 stars
        Price: $49.99

        Product 2:
        Title: Compact Coffee Grinder
        Rating: 4.3 out of 5 stars
        Price: $39.99
    """
    for idx, product in enumerate(products, 1):
        print(f"Product {idx}:")
        print(f"  Title: {product.get('title', 'N/A')}")
        print(f"  Rating: {product.get('rating', 'N/A')}")
        print(f"  Price: {product.get('price')}")
        print()
