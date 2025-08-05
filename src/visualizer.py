# src/visualizer.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging
from pathlib import Path

class BookVisualizer:
    def __init__(self):
        self.cleaned_data_path = Path("data/cleaned_books.csv")

    def plot_publish_years(self):
        try:
            df = pd.read_csv(self.cleaned_data_path)
            plt.figure(figsize=(12, 6))
            sns.countplot(data=df, x="first_publish_year", order=sorted(df["first_publish_year"].dropna().unique()))
            plt.xticks(rotation=90)
            plt.title("Number of Books by First Publish Year")
            plt.tight_layout()
            plt.savefig("data/publish_year_plot.png")
            logging.info("Visualization saved.")
            plt.show()
        except Exception as e:
            logging.error(f"Error generating plot: {e}")
