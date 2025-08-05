# Open Library Fiction Book ETL

This project fetches the top 100 fiction books from OpenLibrary, cleans and stores the data, and visualizes trends by publication year.

## Structure
- `BookFetcher`: Gets raw data from OpenLibrary API
- `BookCleaner`: Cleans the dataset
- `BookDatabase`: Stores data in SQLite
- `BookVisualizer`: Generates visual analytics

## How to Run
```bash
python main.py



---

## 📌 Final Touches

- ✅ Add `.gitignore`: `venv/`, `__pycache__/`, `.DS_Store`, `*.db`
- ✅ Use `try/except` and `logging` in all classes
- ✅ Optional: Add CLI args to run specific stages
- ✅ Bonus: Store API response metadata (timestamp, count, etc.)

---

## 🚧 Future Ideas

- Add unit tests with `pytest`
- Add support for other genres
- Schedule with `cron` or `Airflow`
- Export final data to Google Sheets or Power BI

