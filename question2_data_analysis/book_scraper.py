import requests
import time
import random
import os
import csv

from bs4 import BeautifulSoup

BASE_URL = 'https://books.toscrape.com/catalogue/page-{}.html'
DETAIL_BASE_URL = 'https://books.toscrape.com/catalogue/'
DATA_PATH = "question2_data_analysis/data/"

def fetch_with_retries(url: str, retries: int = 3, timeout: int = 10) -> requests.Response:
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()  # Check if the request was successful
            response.encoding = "utf-8"
            
            return response.text
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == retries:
                print("All attempts failed. Giving up.")
            time.sleep(random.uniform(1, 2))  # Wait a random amount of time before retrying

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

def save_to_csv(data: list, file_name: str = "books_data.csv"):
    headers = ["Title", "Price", "Rating", "Category", "Availability"]
    # Create the csv saving folder if it is not exist
    os.makedirs(DATA_PATH, exist_ok=True)
    
    filepath = DATA_PATH + file_name
    
    with open(filepath, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
    
    print(f"\n-- Data saved to {filepath} --")

def scrape_book_data(pages: int = 5) -> list:
    books_data = []
    for page in range(1, pages + 1):
        url = BASE_URL.format(page)
        print(f"\n-- Scraping book data from Page: {page} --")
        
        try:
            response = fetch_with_retries(url)
            if response is None:
                continue
            
            soup = BeautifulSoup(response, 'html.parser')
            books = soup.find_all("article", class_="product_pod")
            
            for book in books:
                try:
                    title = book.h3.a['title']
                    price = book.find("p", class_="price_color").text.strip()
                    rating = book.find("p", class_="star-rating")["class"][1]
                    category = get_category(DETAIL_BASE_URL + book.h3.a["href"])
                    availability = book.find("p", class_="instock availability").text.strip()
                    
                    books_data.append([
                        title,
                        price,
                        rating,
                        category,
                        availability
                    ])
                    
                    print(f"Scraped: {title}")
                except Exception as book_error:
                    print(f"Error: {book_error}")
                    
            time.sleep(random.uniform(1,2))
            
        except Exception as page_error:
            print(f"Error: {page_error}")
            
    print(f"\n-- {len(books_data)} books was scraped --")
    return books_data

if __name__ == "__main__":
    books_data = scrape_book_data(5)
    save_to_csv(books_data, "books_data.csv")