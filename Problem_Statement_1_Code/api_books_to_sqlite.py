"""
AccuKnox AI/ML Assignment
Problem Statement 1: API Data Retrieval and Storage

This script:
1. Tries to fetch book data from an external API
2. Falls back to simulated data if API is unavailable
3. Stores data into a local SQLite database
"""

import sqlite3
import requests

# -----------------------------
# CONFIG
# -----------------------------
API_URL = "https://example.com/api/books"  # Dummy API (fallback will be used)
DB_PATH = "accuknox.db"

# -----------------------------
# DATABASE SETUP
# -----------------------------
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER
        )
    """)

# -----------------------------
# INSERT DATA
# -----------------------------
def insert_books(cursor, books):
    for book in books:
        cursor.execute(
            """
            INSERT INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
            """,
            (
                book.get("title"),
                book.get("author"),
                book.get("year")
            )
        )

# -----------------------------
# FETCH DATA FROM API
# -----------------------------
def fetch_books_from_api():
    """
    Attempts to fetch data from a real API.
    Falls back to simulated data if API fails.
    """
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        print("✅ Data fetched from real API")
        return response.json()

    except Exception:
        print("⚠️ API not reachable. Using simulated data.")
        return [
            {"title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
            {"title": "Deep Learning", "author": "Ian Goodfellow", "year": 2016},
            {"title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "year": 2017}
        ]

# -----------------------------
# MAIN FUNCTION
# -----------------------------
def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    create_table(cursor)

    books = fetch_books_from_api()
    insert_books(cursor, books)

    conn.commit()
    conn.close()

    print("✅ Books data stored successfully in SQLite database")

# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()
