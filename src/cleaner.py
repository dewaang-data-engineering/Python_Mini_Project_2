# src/cleaner.py
import pandas as pd
import json
import logging
from pathlib import Path

class BookCleaner:
    def __init__(self):
        self.raw_data_path = Path("data/raw_books.json")
        self.cleaned_data_path = Path("data/cleaned_books.csv")

    def clean_data(self):
        try:
            logging.info("Cleaning data...")
            with open(self.raw_data_path) as f:
                raw = json.load(f)

            df = pd.DataFrame(raw)

            # Ensure required columns exist
            required_cols = ["title", "author_name", "first_publish_year"]
            for col in required_cols:
                if col not in df.columns:
                    df[col] = None

            # Optional column: ratings_sortable
            if "ratings_sortable" not in df.columns:
                df["ratings_sortable"] = None

            # Filter only the columns we care about
            df = df[["title", "author_name", "first_publish_year", "ratings_sortable"]]

            # Drop rows missing essential fields (but not rating)
            df = df.dropna(subset=["title", "author_name", "first_publish_year"])

            # Format author_name list into string
            df["author_name"] = df["author_name"].apply(lambda x: ", ".join(x) if isinstance(x, list) else str(x))

            # Save cleaned data
            df.to_csv(self.cleaned_data_path, index=False)
            logging.info("Cleaned data saved.")
            return df

        except Exception as e:
            logging.error(f"Error cleaning data: {e}")
            return pd.DataFrame()
