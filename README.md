# AccuKnox AI/ML Assignment – Problem Statement 1

## Candidate Details
Name: Jatavath Arjun Kumar  
Degree: B.Tech – Civil Engineering  
Institute: NIT Warangal  

---

## Overview
This repository contains my solution for **Problem Statement 1** of the AccuKnox AI/ML assignment.

The objective of this assignment is to demonstrate my ability to:
- Work with external data sources (APIs and CSV files)
- Store structured data using SQLite
- Perform basic data processing
- Visualize data for quick insights
- Write clean, readable, and explainable Python code

I intentionally focused on **building a reliable and clear data pipeline first**, without over-engineering the solution.

---

## Problem Statement Summary
The assignment consists of three parts:

1. Fetch data from an external REST API and store it in a SQLite database  
2. Import data from a CSV file into a SQLite database  
3. Process student score data and visualize it using a bar chart  

Each part is implemented as a separate Python script to maintain clarity and modularity.

---

## Project Structure
AccuKnox_AI_ML_Assignment
│
├── Problem_Statement_1_Code
│ ├── api_books_to_sqlite.py
│ ├── csv_to_sqlite.py
│ ├── student_scores_visualization.py
│ └── README.md
│
├── data
│ └── user.csv
│
├── databse
│ └── accknox.db
│
├── Assignment_Document
│ └── Accuknox_Assignment.docx
│
├── GitHub_Links
│ ├── complex_python_code.txt
│ └── complex_database_code.txt
│
└── Resume
└── Arjun_Resume.pdf

yaml
Copy code

---

## Detailed Implementation Explanation

### 1. API Data Retrieval and Storage
**File:** `api_books_to_sqlite.py`

What this script does:
- Attempts to fetch book data from an external REST API
- Handles API failures gracefully using exception handling
- Uses fallback sample data when the API is unavailable
- Stores the data (title, author, publication year) into a SQLite database

Why this approach:
- External APIs can be unreliable, so fallback logic keeps the pipeline functional
- SQLite is sufficient for local testing and small-scale data storage
- Clear separation between API logic and database logic improves readability

---

### 2. CSV Data Import into SQLite
**File:** `csv_to_sqlite.py`

What this script does:
- Reads user data from a CSV file
- Creates a users table in SQLite with basic constraints
- Inserts CSV data into the database
- Skips duplicate records using a UNIQUE constraint on email

Why this approach:
- CSV-to-database ingestion is a common real-world ETL task
- Database-level constraints help maintain data integrity
- Exception handling ensures the script does not crash on bad input

---

### 3. Data Processing and Visualization
**File:** `student_scores_visualization.py`

What this script does:
- Uses simulated student score data
- Calculates basic statistics (average, minimum, maximum)
- Visualizes the scores using a bar chart
- Saves the chart as an image file for reference

Why a bar chart:
- Makes it easy to compare scores between students
- The average line helps quickly understand overall performance

---

## Assumptions
- External APIs may be unavailable, so simulated data is acceptable
- SQLite is sufficient for demonstrating database logic
- Data size is small to moderate
- No authentication is required for the APIs
- Focus is on correctness and clarity rather than production-level optimization

---

## How to Run the Code

### Step 1: Install Dependencies
pip install -r requirements.txt

graphql
Copy code

### Step 2: Run API to SQLite Script
python Problem_Statement_1_Code/api_books_to_sqlite.py

graphql
Copy code

### Step 3: Run CSV to SQLite Script
python Problem_Statement_1_Code/csv_to_sqlite.py

graphql
Copy code

### Step 4: Run Data Processing and Visualization Script
python Problem_Statement_1_Code/student_scores_visualization.py

yaml
Copy code

---

## Technologies Used
- Python  
- SQLite  
- Requests  
- Pandas  
- Matplotlib  

---

## Possible Improvements and Next Steps
If this system were extended further, I would:
- Add structured logging instead of print statements
- Implement retry mechanisms for API failures
- Perform deeper statistical analysis on the data
- Integrate a machine learning model once the data pipeline is stable and validated

---

## Final Note
This assignment reflects my current level of understanding of Python-based data handling and basic analytics.  
I focused on clarity, robustness, and explainability, while keeping clear scope for future AI/ML enhancements.

---

End of submission.
