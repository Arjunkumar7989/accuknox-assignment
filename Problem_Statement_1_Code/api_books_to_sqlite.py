import sqlite3
import requests
import logging
import os
from statistics import mean
from typing import List, Dict

# ---------------------------------
# CONFIGURATION
# ---------------------------------
API_URL = "https://example.com/api/books"   # Assumed external API
DB_PATH = "database/accuknox.db"
LOG_FILE = "pipeline.log"
REQUEST_TIMEOUT = 5

# ---------------------------------
# LOGGING SETUP
# ---------------------------------
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ---------------------------------
# DATABASE SETUP
# ---------------------------------
def create_table(cursor: sqlite3.Cursor) -> None:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER,
            UNIQUE(title, author)
        )
    """)
    logging.info("Database table 'books' ensured")

# ---------------------------------
# API DATA FETCH WITH FALLBACK
# ---------------------------------
def fetch_books_from_api() -> List[Dict]:
    try:
        response = requests.get(API_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("API returned invalid or empty data")

        logging.info("Data fetched successfully from API")
        return data

    except (requests.exceptions.RequestException, ValueError) as e:
        logging.warning(f"API failure: {e}. Using fallback data.")

        return [
            {"title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
            {"title": "Deep Learning", "author": "Ian Goodfellow", "year": 2016},
            {"title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "year": 2017}
        ]

# ---------------------------------
# DATA VALIDATION
# ---------------------------------
def validate_book(book: Dict) -> bool:
    return (
        isinstance(book, dict) and
        isinstance(book.get("title"), str) and book["title"].strip() != "" and
        isinstance(book.get("author"), str) and book["author"].strip() != "" and
        isinstance(book.get("year"), int)
    )

# ---------------------------------
# DATA INSERTION
# ---------------------------------
def insert_books(cursor: sqlite3.Cursor, books: List[Dict]) -> int:
    inserted_count = 0

    for book in books:
        if not validate_book(book):
            logging.warning(f"Invalid record skipped: {book}")
            continue

        try:
            cursor.execute(
                """
                INSERT OR IGNORE INTO books (title, author, publication_year)
                VALUES (?, ?, ?)
                """,
                (book["title"], book["author"], book["year"])
            )
            inserted_count += 1

        except sqlite3.Error as e:
            logging.error(f"Database insert error for {book}: {e}")

    logging.info(f"{inserted_count} records processed")
    return inserted_count

# ---------------------------------
# BASIC DATA ANALYSIS (ML-READY)
# ---------------------------------
def analyze_books(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        "SELECT publication_year FROM books WHERE publication_year IS NOT NULL"
    )
    years = [row[0] for row in cursor.fetchall()]

    if not years:
        logging.warning("No data available for analysis")
        print("⚠️ No data available for analysis")
        return

    avg_year = round(mean(years), 2)
    logging.info(f"Average publication year calculated: {avg_year}")
    print(f"📊 Average publication year: {avg_year}")

# ---------------------------------
# MAIN PIPELINE
# ---------------------------------
def main() -> None:
    try:
        # Ensure DB directory exists
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        create_table(cursor)

        books = fetch_books_from_api()
        insert_books(cursor, books)

        analyze_books(cursor)

        conn.commit()
        conn.close()

        logging.info("Pipeline executed successfully")
        print("✅ Books data stored successfully")

    except Exception as e:
        # Generic handler only at orchestration level
        logging.critical(f"Pipeline failed: {e}")
        print("❌ Pipeline execution failed. Check pipeline.log for details.")

# ---------------------------------
# ENTRY POINT
# ---------------------------------
if __name__ == "__main__":
    main()
