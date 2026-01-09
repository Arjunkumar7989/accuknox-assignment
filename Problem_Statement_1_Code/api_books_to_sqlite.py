import sqlite3
import requests

# ---------------------------------
# CONFIGURATION
# ---------------------------------
API_URL = "https://example.com/api/books"  # External API (assumed)
DB_PATH = "databse/accknox.db"

# ---------------------------------
# DATABASE SETUP
# ---------------------------------
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER
        )
    """)

# ---------------------------------
# DATA INSERTION
# ---------------------------------
def insert_books(cursor, books):
    for book in books:
        # Basic validation before insert
        if "title" in book and "author" in book:
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

# ---------------------------------
# API DATA FETCH
# ---------------------------------
def fetch_books_from_api():
    """
    Attempts to fetch data from an external API.
    Falls back to simulated data if the API is unavailable.
    """
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        print("Data fetched successfully from API")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        print("Using fallback sample data")

        # Fallback data to keep pipeline functional
        return [
            {"title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
            {"title": "Deep Learning", "author": "Ian Goodfellow", "year": 2016},
            {"title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "year": 2017}
        ]

# ---------------------------------
# MAIN EXECUTION
# ---------------------------------
def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    create_table(cursor)

    books = fetch_books_from_api()
    insert_books(cursor, books)

    conn.commit()
    conn.close()

    print("Books data stored successfully in SQLite database")

# ---------------------------------
# ENTRY POINT
# ---------------------------------
if __name__ == "__main__":
    main()
