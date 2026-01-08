import csv
import sqlite3

CSV_PATH = "data/users.csv"
DB_PATH = "database/accuknox.db"


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)

    with open(CSV_PATH, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (row["name"], row["email"])
            )

    conn.commit()
    conn.close()

    print("CSV data inserted into SQLite successfully.")


if __name__ == "__main__":
    main()
