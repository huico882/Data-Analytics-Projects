# Data Analytics Projects
This is a collection of data analytic projects I have completed. Some tools used include SQL, Excel, Python, and Tableau.

## Projects
- [Amazon Product Description Generator (APDG)]
   - [Background]
   - [Process]
   - [Workflow]
- [Olist E-Commerce Sales Analysis](https://github.com/huico882/Data-Analytics-Projects/blob/main/README.md#olist-e-commerce-sales--marketing-analysis)
   - [Background](https://github.com/huico882/Data-Analytics-Projects/blob/main/README.md#olist-e-commerce-background)
   - [Process](https://github.com/huico882/Data-Analytics-Projects/blob/main/README.md#process-for-olist-e-commerce-analysis)
   - [Sales Analysis](https://github.com/huico882/Data-Analytics-Projects/blob/main/README.md#olist-e-commerce-sales-analysis)
     - [Dashboard](https://github.com/huico882/Data-Analytics-Projects/blob/main/README.md#sales-analysis-dashboard)
     - [Key Insights](https://github.com/huico882/Data-Analytics-Projects/blob/main/README.md#sales-analysis-key-insights)
   - [Key Takeaways](https://github.com/huico882/Data-Analytics-Projects/blob/main/README.md#olist-e-commerce-key-takeaways)

- [Billboard Top 100 Analysis of Audio Features](#billboard-top-100-analysis-of-audio-features)
   - [Process](#process-for-billboard-analysis)
   - [Dashboard](#billboard-top-100-analysis-of-audio-features-dashboard)


## Amazon Product Description Generator

### (APDG) Background
The Amazon Product Description Generator is a Python-based tool designed to scrape product data from Amazon, analyze key metrics (like price, title length, and word count), and generate optimized Amazon product descriptions, titles, prices, and SEO keywords using AI. This project leverages libraries such as BeautifulSoup for web scraping, pandas for data analysis, and the ollama package for AI integration.

### (APDG) Process
1. **Web Scraping**: Implemented a tool that pulls product information from Amazon using `requests` to fetch the webpage and `BeautifulSoup` to parse the HTML content.
   - Headers were configured to simulate a browser request and avoid detection.
   - Functions were developed to pull website content, parse HTML, extract product information, and convert it into usable formats.

2. **Data Analysis**: Analyzed product data such as average title size, most common word counts, median prices, and more using `pandas`.
   - Created functions to calculate the character size of titles, word counts, and price statistics.
   - Ensured that non-numerical prices (e.g., "N/A") were filtered out for accurate analysis.

3. **AI-Powered Generation**: Used the Ollama `llama3.1:8b` model to generate optimized product descriptions.
   - Integrated AI to generate five distinct product descriptions based on the analysis of scraped data.
   - This step involved crafting a detailed prompt that included insights from the scraped and analyzed data, such as average title lengths, price ranges, and SEO keywords.


### Example Workflow

1. Run the script and provide a product title and description as input:

   ```plaintext
   Enter the product title: Coffee Grinder

   Enter the product description: A sleek black coffee grinder with multiple grind settings.
   ```
2. The tool scrapes Amazon, analyzes data, and generates AI-based suggestions. Example output:

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

### Technologies Used
- **Python Libraries**:
  - `BeautifulSoup`: Web scraping
  - `pandas`: Data manipulation and analysis
  - `ollama`: AI model integration
  - `requests`: HTTP requests for web scraping

- **AI Model**:
  - Llama `llama3.1:8b` (via `ollama`)



## Olist E-Commerce Sales Analysis

### Olist E-Commerce Background
   - Olist is an E-commerce store located in Brazil.
   - The data analyzed ranges from August 2016 to August 2018. There was a little bit more data available but the information was not updated so, to make the analysis consistent, I stopped using data after August 2018
   - Olist is an online marketplace where small businesses in Brazil are easily able to sell their products. For more information, visit the [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data?select=olist_sellers_dataset.csv) where the data was pulled from.
      

#### Process For Olist E-Commerce Analysis
1. Download Olist E-Commerce Dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data?select=olist_sellers_dataset.csv)
2. Assessed the database, and looked at the relationship between the datasets. I noticed that there was a list of product categories but that they were in Portuguese. Since the database also included a translation of the product categories, I decided to create a new dataset in English
      ![Olist_database](https://github.com/user-attachments/assets/a171250e-eede-41c8-a47b-de32cc616147)
3. Import the `olist_products_dataset` and `product_category_name_translation` datasets into SQLite. Then run the following code to create a new table,
```
      CREATE TABLE olist_products_dataset_translated AS
      SELECT 
      	s.product_id,
      	t.product_category_name_english,
      	s.product_name_lenght,
      	s.product_description_lenght,
      	s.product_photos_qty
      FROM olist_products_dataset as s
      LEFT JOIN product_category_name_translation as t
      ON s.product_category_name = t.product_category_name
      WHERE s.product_category_name IS NOT NULL;
```
4. while playing with the SQL code, I noticed that some product categories in `olist_products_dataset` were null values. To deal with this, I included the code `WHERE s.product_category_name IS NOT NULL` which will only include products that have a product category
5. After joining the tables together, I exported the data and inserted all relevant information into Tableau. From here, I did any sort of analysis and visuals that were needed

### Olist E-Commerce Sales Analysis
#### [Sales Analysis Dashboard](https://public.tableau.com/views/OlistE-Commerce_17356217424300/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
   ![Dashboard 1 (3)](https://github.com/user-attachments/assets/b318722b-2ee4-45ce-af63-bfec4109e8e7)


##### Sales Analysis Key Insights
   - The highest-selling month was November 2017, this aligns with Black Friday, which is when stores have a lot of discounts and consumers are willing to spend money.
   - The most revenue generated categories include (starting from most) Health Beauty, Watches Gifts, Bed Bath Table, Computer Accessories, and Sports Leisure.
   - The least revenue generated categories include (starting from least) Security & Services, Fashion Childrens Clothes, "CDs, DVDs, & Musicals", Home Comfort 2, and Flowers
   - The most sold categories by quantity include (starting from most) Bed Bath Table, Furniture Decor, Health Beauty, Sports Leisure, and Computer Accessories.
   - The least sold categories by quantity include (starting from least) Security & Services, Fashion Childrens Clothes, "CDs, DVDs & Musicals", Cousine, Arts & Craftsmanship.
   - The most revenue generated State and City was Sao Paulo by far. This state generated 3x more than the second state, Rio de Janeiro.

### Olist E-Commerce Key Takeaways
   - The E-Commerce store should focus on their Health Beauty & Fitness sections. These categories generated some of the best revenues while having a lower # of items sold.
   - Watches is also among this group, it generated the second most revenue while having sold half as much as the most sold item by quantity, Bed Bath Table.
   - Focusing on Health, Beauty, Fitness, & Fashion (specifically accessories, such as watches) are key to generating more revenue.
   - Although some Fashion categories such as Childrens Clothes and Sports are in the lower spectrum in terms of quantity sold and revenue generated, if focusing on the categories mentioned in the point above, it would be beneficial to revamp these categories. There is a lot of potential revenue if Olist improves and markets Fashion in Childrens Clothes and Sports.
   - Marketing should be increased in Rio de Janeiro. It already has the second most revenue, and focusing on promoting E-Commerce more in the State, has the potential to significantly increase revenue.





## Billboard Top 100 Analysis of Audio Features

### Process For Billboard Analysis
1. Download the files Billboard (includes Billboard Top 100 since 1958) and the Spotify audio features from [Kaggle](https://www.kaggle.com/datasets/sujaykapadnis/top-100-billboard).
2. Download SQLite to join both sheets using the identifiers: song and performers. Include features such as key, tempo, and danceability with data such as the date, and week position that were on Billboard.
3. Once both CSV files have been imported to SQLite, Use the following code to join and create a new table called `billboard_audio_features`
   ```
       CREATE TABLE billboard_audio_features AS
       SELECT
        b.*,
        s.tempo,
        s.key,
        s.danceability,
            s.energy,
            s.loudness,
            s.speechiness,
            s.acousticness,
            s.instrumentalness,
            s.liveness,
            s.valence
       FROM billboard AS b
       LEFT JOIN audio_features AS s
           ON b.song = s.song
           AND b.performer = s.performer;
   ```
4. Once the SQL code has been executed and the table has been created, export the table from SQLite and import the CSV file to Tableau.
5. From here, create any analysis and visuals for dashboard!

### [Billboard Top 100 Analysis of Audio Features Dashboard](https://public.tableau.com/views/BillboardTop100AudioFeatures/Dashboard2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

   ![Dashboard 2](https://github.com/user-attachments/assets/7d9c39ea-ef48-4a4b-9ec7-a81909ed1f31)


