# src/database.py
import sqlite3
import pandas as pd
import logging
from pathlib import Path

class BookDatabase:
    def __init__(self):
        self.db_path = Path("db/books.db")
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.table_name = "fiction_books"
        self.create_table()

    def create_table(self):
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                first_publish_year INTEGER,
                rating REAL
            );
        """)
        self.conn.commit()
        logging.info("Table created or verified.")

    def insert_books(self, df: pd.DataFrame):
        try:
            df.to_sql(self.table_name, self.conn, if_exists="replace", index=False)
            logging.info(f"Inserted {len(df)} books into DB.")
        except Exception as e:
            logging.error(f"Error inserting books: {e}")
