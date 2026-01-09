import csv
import sqlite3
import os
import logging
from collections import Counter
from typing import Dict

# -----------------------------
# CONFIGURATION
# -----------------------------
CSV_PATH = "data/user.csv"
DB_PATH = "database/accuknox.db"
LOG_FILE = "csv_pipeline.log"

# -----------------------------
# LOGGING SETUP
# -----------------------------
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# -----------------------------
# DATA VALIDATION
# -----------------------------
def validate_row(row: Dict) -> bool:
    return (
        isinstance(row.get("name"), str) and row["name"].strip() != "" and
        isinstance(row.get("email"), str) and "@" in row["email"]
    )

# -----------------------------
# BASIC DATA ANALYSIS (AI-READY)
# -----------------------------
def analyze_users(cursor: sqlite3.Cursor) -> None:
    cursor.execute("SELECT email FROM users")
    domains = [row[0].split("@")[-1] for row in cursor.fetchall()]

    if not domains:
        logging.warning("No data available for analysis")
        print("⚠️ No data available for analysis")
        return

    domain_counts = Counter(domains)
    most_common_domain, count = domain_counts.most_common(1)[0]

    logging.info(f"Most common email domain: {most_common_domain} ({count})")
    print(f"📊 Most common email domain: {most_common_domain} ({count})")

# -----------------------------
# MAIN PIPELINE
# -----------------------------
def main() -> None:
    try:
        # Ensure DB directory exists
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)
        logging.info("Users table ensured")

        inserted_count = 0
        skipped_count = 0
        invalid_count = 0

        # Read CSV
        with open(CSV_PATH, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            if not reader.fieldnames or "name" not in reader.fieldnames or "email" not in reader.fieldnames:
                raise ValueError("CSV missing required columns: name, email")

            for row in reader:
                if not validate_row(row):
                    invalid_count += 1
                    logging.warning(f"Invalid row skipped: {row}")
                    continue

                try:
                    cursor.execute(
                        "INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)",
                        (row["name"].strip(), row["email"].strip())
                    )
                    inserted_count += 1
                except sqlite3.Error as e:
                    logging.error(f"Insert failed for {row}: {e}")

        analyze_users(cursor)

        conn.commit()
        conn.close()

        logging.info("CSV pipeline executed successfully")

        print(
            f"✅ CSV import completed | "
            f"Inserted: {inserted_count}, "
            f"Invalid: {invalid_count}, "
            f"Duplicates ignored"
        )

    except FileNotFoundError:
        logging.critical("CSV file not found")
        print("❌ CSV file not found. Please check the file path.")

    except ValueError as ve:
        logging.critical(f"CSV structure error: {ve}")
        print(f"❌ CSV error: {ve}")

    except sqlite3.Error as db_error:
        logging.critical(f"Database error: {db_error}")
        print("❌ Database error occurred. Check logs.")

    except Exception as e:
        logging.critical(f"Unexpected pipeline failure: {e}")
        print("❌ Unexpected error occurred. Check logs.")

# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()
