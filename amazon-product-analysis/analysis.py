import pandas as pd


def description_charSize(titles):
    """
    Calculate character size statistics for a list of titles.

    This function computes the mean, median, and mode of character lengths for
    a list of product titles.

    Args:
        titles (list[str]): A list of product titles.

    Returns:
        tuple: A tuple containing:
            - mean (float): The average character length of the titles.
            - median (float): The median character length of the titles.
            - mode (list[float]): The mode(s) of character lengths as a list.

    Example:
        >>> titles = ["Product A", "Product B", "Long Product Title"]
        >>> description_charSize(titles)
        (15.0, 11.0, [11.0])
    """
    # Calculate the character lengths for each title
    char_sizes = [len(title) for title in titles]

    # Create a Pandas Series
    series = pd.Series(char_sizes)

    # Calculate statistics
    mean = float(round(series.mean(), 0))
    median = float(round(series.median(), 0))
    mode = [float(m) for m in series.mode()]  # List of modes

    return mean, median, mode


def description_wordCount(titles):
    """
    Calculate word count statistics for a list of titles.

    This function computes the mean, median, and mode of word counts for
    a list of product titles.

    Args:
        titles (list[str]): A list of product titles.

    Returns:
        tuple: A tuple containing:
            - mean (float): The average word count of the titles.
            - median (float): The median word count of the titles.
            - mode (list[float]): The mode(s) of word counts as a list.

    Example:
        >>> titles = ["Product A", "Product B", "Long Product Title"]
        >>> description_wordCount(titles)
        (2.0, 2.0, [2.0])
    """
    # Calculate the character lengths for each title
    total_words = [len(title.split()) for title in titles]

    # Create a Pandas Series
    series = pd.Series(total_words)

    # Calculate statistics
    mean = float(round(series.mean(), 0))
    median = float(round(series.median(), 0))
    mode = [float(m) for m in series.mode()]  # List of modes

    return mean, median, mode


# ------PRICES------------------------------------

def price_stats(prices):
    """
    Calculate price statistics for a list of prices.

    This function computes the lowest price, highest price, mean, median, and mode
    from a list of price strings. It filters out invalid price strings before processing.

    Args:
        prices (list[str]): A list of price strings (e.g., "$19.99", "$25.49").

    Returns:
        tuple: A tuple containing:
            - low (float): The lowest price.
            - high (float): The highest price.
            - mean (float): The average price.
            - median (float): The median price.
            - mode (list[float]): The mode(s) of prices as a list.

    Example:
        >>> prices = ["$19.99", "$25.49", "$25.49", "$39.99"]
        >>> price_stats(prices)
        (19.99, 39.99, 27.74, 25.0, [25.0])
    """
    prices_cleaned = [
        float(price[1:]) for price in prices
        if price.startswith('$') and price[1:].replace('.', '', 1).isdigit()
    ]

    # Sort the prices in ascending order
    sorted_prices = sorted(prices_cleaned)

    # Create a Pandas Series
    series = pd.Series(sorted_prices)

    # Calculate statistics
    mean = float(round(series.mean(), 2))
    median = float(round(series.median(), 0))
    mode = [float(round(m, 0)) for m in series.mode()]
    low = float(sorted_prices[0])
    high = float(sorted_prices[len(sorted_prices) - 1])

    return low, high, mean, median, mode
