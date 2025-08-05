# main_py.py

from src.fetcher import BookFetcher
from src.cleaner import BookCleaner
from src.database import BookDatabase
from src.visualizer import BookVisualizer

import logging

logging.basicConfig(
    filename="logs/book_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def run_pipeline():
    fetcher = BookFetcher()
    raw_books = fetcher.fetch_books()

    cleaner = BookCleaner()
    cleaned_df = cleaner.clean_data()

    db = BookDatabase()
    db.insert_books(cleaned_df)

    viz = BookVisualizer()
    viz.plot_publish_years()

if __name__ == "__main__":
    run_pipeline()
