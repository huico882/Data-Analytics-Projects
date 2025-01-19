# Amazon Product Description Generator

## Overview
The **Amazon Product Description Generator** is a Python-based tool designed to scrape product data from Amazon, analyze key metrics (like price, title length, and word count), and generate optimized Amazon product descriptions, titles, prices, and SEO keywords using AI. This project leverages libraries such as `BeautifulSoup` for web scraping, `pandas` for data analysis, and the `ollama` package for AI integration.

## Features
- **Web Scraping**: Extracts product information such as titles, prices, and ratings from Amazon search results.
- **Data Analysis**: Computes statistical metrics (mean, median, mode) for product titles, word counts, and prices.
- **AI Integration**: Generates compelling Amazon product descriptions and SEO-friendly titles using the `ollama` AI model.
- **Customizable**: Allows users to input a product title and description to tailor the generated content.

## How It Works
1. **Input**: Users provide a product title and description.
2. **Scraping**: The tool scrapes Amazon for similar products and collects data such as titles, ratings, and prices.
3. **Analysis**: Statistical metrics are computed to understand trends in similar products.
4. **Prompt Generation**: Insights from the data are passed into an AI model as part of a structured prompt.
5. **Output**: The AI generates five optimized product descriptions in JSON format.

## Installation

### Prerequisites
- Python 3.9+
- Virtual environment setup (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd AmazonProductDescriptionGenerator
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure the `ollama` package is set up with the required model (e.g., `llama3.1:8b`). Refer to the [Ollama documentation](https://ollama.com/docs) for guidance.

## Usage
Run the script to generate Amazon product descriptions:

```bash
python3 main.py
```

### Example Interaction
1. You will be prompted to enter a product title and description:
   ```plaintext
   Enter the product title: Coffee Grinder
   Enter the product description: A sleek black coffee grinder with multiple grind settings.
   ```

2. The tool scrapes Amazon, analyzes data, and outputs:
   ```json
   {
       "products_desc_list": [
           {
               "title": "Sleek Black Coffee Grinder - Multiple Grind Settings",
               "description": "Elevate your coffee game with our sleek black grinder. Perfect for any brew.",
               "price": "$49.99",
               "seo": "coffee grinder, sleek design, grind settings"
           },
           ...
       ]
   }
   ```

## Project Structure
```
AmazonProductDescriptionGenerator/
├── analysis.py          # Functions for data analysis (e.g., mean, median, mode)
├── scraper.py           # Web scraping logic for extracting product data
├── ai.py                # AI model integration and prompt generation
├── requirements.txt     # Python dependencies
├── main.py              # Main entry point for running the program
├── README.md            # Project documentation
└── venv/                # Virtual environment folder (optional)
```

## Technologies Used
- **Python Libraries**:
  - `BeautifulSoup`: Web scraping
  - `pandas`: Data manipulation and analysis
  - `ollama`: AI model integration
  - `requests`: HTTP requests for web scraping

- **AI Model**:
  - Llama `llama3.1:8b` (via `ollama`)

## Limitations
- The tool relies on web scraping, which may result in issues if Amazon's HTML structure changes.
- Amazon may block requests if too many are made in a short period. Consider using a proxy or rate-limiting.
- Requires the `ollama` AI model to be set up locally.

## Future Improvements
- Enhance error handling for failed requests or unexpected HTML structures.
- Add support for more e-commerce platforms.
- Implement a GUI or web-based interface for ease of use.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [Ollama AI Models](https://ollama.com/models)

---

Feel free to reach out for questions or contributions!

