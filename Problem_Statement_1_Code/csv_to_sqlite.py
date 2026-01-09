import csv
import sqlite3
import os

# -----------------------------
# CONFIGURATION
# -----------------------------
CSV_PATH = "data/user.csv"
DB_PATH = "databse/accknox.db"

# -----------------------------
# MAIN FUNCTION
# -----------------------------
def main():
    try:
        # Ensure database directory exists
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create users table with basic constraints
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE
            )
        """)

        inserted_count = 0
        skipped_count = 0

        # Read CSV and insert data
        with open(CSV_PATH, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    cursor.execute(
                        "INSERT INTO users (name, email) VALUES (?, ?)",
                        (row["name"], row["email"])
                    )
                    inserted_count += 1
                except sqlite3.IntegrityError:
                    # Skip duplicate emails
                    skipped_count += 1

        conn.commit()
        conn.close()

        print(f"CSV import completed. Inserted: {inserted_count}, Skipped duplicates: {skipped_count}")

    except FileNotFoundError:
        print("CSV file not found. Please check the file path.")
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()
