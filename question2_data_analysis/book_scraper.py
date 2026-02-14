"""
book_scraper.py
This script scrapes book data from the "https://books.toscrape.com" website, 
including title, price, rating, category, and availability. 
The scraped data is saved to a CSV file for further analysis.
"""

import requests
import time
import random
import os
import csv

from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_URL = 'https://books.toscrape.com/catalogue/page-{}.html' # URL template for paginated book listings
DETAIL_BASE_URL = 'https://books.toscrape.com/catalogue/' # Base URL for further book details
DATA_PATH = "question2_data_analysis/data/raw/" # Path to save the scraped data

"""
Define a function to fetch the content of the URL
Parameters:
    url (str): The URL to fetch
    retries (int): The number of retry attempts if failed
    timeout (int): The timeout for the request in seconds
Structure:
- Try to fetch the URL content
- If successful, return the response text
- If an error occurs, print the error and retry until the maximum number of retries is reached
Return:
- The response text if successful, or None if all attempts fail
"""
def fetch_with_retries(url: str, retries: int = 3, timeout: int = 10) -> requests.Response:
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()  # Check if the request was successful
            response.encoding = "utf-8" # Encode the response to UTF-8 to handle special characters
            
            return response.text
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == retries:
                print("All attempts failed. Giving up.")
            time.sleep(random.uniform(1, 2))  # Wait a random amount of time before retrying

"""
Define a function to extract the category of a book from its detail URL
Parameters:
    detail_url (str): The URL of the book's detail page
Structure:
- Try to fetch the detail page content
- If successful, parse the HTML and extract the category from the breadcrumb navigation
- If an error occurs, return "Unknown"
Return:
    The category name as a string, or "Unknown" if extraction fails
"""
def get_category(detail_url: str) -> str:
    try:
        response = fetch_with_retries(detail_url)
        if response is None:
            return "Unknown"
        
        soup = BeautifulSoup(response, "html.parser")
        breadcrumb = soup.find("ul", class_="breadcrumb")
        category = breadcrumb.find_all("li")[2].text.strip()
        return category
    except Exception as e:
        print(f"Error: {e}")
        return 'Unknown'

"""
Define a function to save the scraped data to a CSV file
Parameters:
    data (list): A list of lists containing the book data
    file_name (str): The name of the CSV file to save the data to
Structure:
- Define the headers for the CSV file
- Create the directory for saving the CSV file if it does not exist
- Open the CSV file for writing and write the headers and data rows
- Print a confirmation message with the file path
"""
def save_to_csv(data: list, file_name: str = "books_data.csv"):
    headers = ["title", "price", "rating", "category", "availability"]
    # Create the csv saving folder if it is not exist
    os.makedirs(DATA_PATH, exist_ok=True)
    
    filepath = DATA_PATH + file_name
    
    with open(filepath, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
    
    print(f"\n-- Data saved to {filepath} --")

"""
Define a function to scrape book data from the website
Parameters:
    pages (int): The number of pages to scrape (default is 5)
Structure:
- Initialize an empty list to store the scraped book data
- Loop through the number of pages
- Construct the URL and fetch the page content
- Extract the data tile, price, rating, category and availability
- Append the data into book data list
Return:
- A list of lists containing the scraped book data
"""
def scrape_data(pages: int = 5) -> list:
    scraped_data = []
    for page in tqdm(range(1, pages + 1), desc="Scraping Pages"):
        url = BASE_URL.format(page)
        
        try:
            response = fetch_with_retries(url)
            if response is None:
                continue
            
            soup = BeautifulSoup(response, 'html.parser')
            books = soup.find_all("article", class_="product_pod")
            
            for book in tqdm(books, desc=f"Processing Page {page}", leave=False):
                try:
                    title = book.h3.a['title']
                    price = book.find("p", class_="price_color").text.strip()
                    rating = book.find("p", class_="star-rating")["class"][1]
                    category = get_category(DETAIL_BASE_URL + book.h3.a["href"])
                    availability = book.find("p", class_="instock availability").text.strip()
                    
                    scraped_data.append([
                        title,
                        price,
                        rating,
                        category,
                        availability
                    ])
                except Exception as book_error:
                    print(f"Error: {book_error}")
            
        except Exception as page_error:
            print(f"Error: {page_error}")
            
    print(f"\n-- {len(scraped_data)} data was scraped --")
    return scraped_data

if __name__ == "__main__":
    books_data = scrape_book_data(5)
    save_to_csv(books_data, "books_data.csv")