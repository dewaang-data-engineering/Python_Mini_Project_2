# src/fetcher.py
import requests
import json
import logging
from pathlib import Path

class BookFetcher:
    def __init__(self):
        self.url = "https://openlibrary.org/search.json?q=subject:fiction&limit=100"
        self.raw_data_path = Path("data/raw_books.json")
        logging.basicConfig(filename="logs/book_pipeline.log", level=logging.INFO)

    def fetch_books(self):
        try:
            logging.info("Fetching data from OpenLibrary API...")
            response = requests.get(self.url)
            response.raise_for_status()

            data = response.json()
            books = data.get("docs", [])
            
            logging.info(f"Fetched {len(books)} books.")
            self.raw_data_path.write_text(json.dumps(books, indent=2))
            return books
        except Exception as e:
            logging.error(f"Error fetching books: {e}")
            return []
