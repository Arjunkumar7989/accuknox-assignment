import requests
import sqlite3

# Assumption:
# Real API may not be accessible, so fallback simulated data is used
API_URL = "https://example.com/api/books"
DB_PATH = "database/accuknox.db"


def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year INTEGER
        )
    """)


def insert_books(cursor, books):
    for book in books:
        cursor.execute(
            "INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)",
            (
                book.get("title"),
                book.get("author"),
                book.get("year")
            )
        )


def fetch_books_from_api():
    """
    Tries to fetch data from API.
    Falls back to simulated data if API is unavailable.
    """
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        print("Data fetched from real API.")
        return response.json()
    except Exception:
        print("API not reachable. Using simulated book data.")
        return [
            {"title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
            {"title": "Deep Learning", "author": "Ian Goodfellow", "year": 2016},
            {
                "title": "Designing Data-Intensive Applications",
                "author": "Martin Kleppmann",
                "year": 2017
            }
        ]


def main():
    print("Starting Book Data Ingestion Process...\n")

    books_data = fetch_books_from_api()

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        create_table(cursor)

        # Clear old data to avoid duplicate inserts
        cursor.execute("DELETE FROM books")

        insert_books(cursor, books_data)
        conn.commit()

        print("\nBooks stored successfully. Displaying records:\n")

        for row in cursor.execute(
            "SELECT title, author, publication_year FROM books"
        ):
            print(row)

    except sqlite3.Error as e:
        print("Database error occurred:", e)

    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")


if __name__ == "__main__":
    main()
