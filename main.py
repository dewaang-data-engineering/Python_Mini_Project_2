# main.py
from src.fetcher import BookFetcher
from src.cleaner import BookCleaner
from src.database import BookDatabase
from src.visualizer import BookVisualizer

import streamlit as st
import pandas as pd

def run_pipeline():
    st.info("🔄 Fetching data from OpenLibrary...")
    fetcher = BookFetcher()
    fetcher.fetch_books()

    st.info("🧹 Cleaning data...")
    cleaner = BookCleaner()
    df = cleaner.clean_data()

    if df.empty:
        st.error("❌ No data after cleaning. Aborting.")
        return

    st.success(f"✅ Cleaned {len(df)} books.")
    st.dataframe(df.head())

    st.info("📦 Inserting into SQLite DB...")
    db = BookDatabase()
    db.insert_books(df)

    st.success("✅ Inserted into database.")

    st.info("📊 Generating plot...")
    viz = BookVisualizer()
    viz.plot_publish_years()

    st.image("data/publish_year_plot.png", caption="Books by First Publish Year")

    st.download_button("⬇️ Download Cleaned CSV", data=df.to_csv(index=False), file_name="cleaned_books.csv", mime="text/csv")

# Streamlit entry point
if __name__ == "__main__":
    st.title("📚 OpenLibrary Fiction Book ETL")
    if st.button("🚀 Run ETL Pipeline"):
        run_pipeline()
