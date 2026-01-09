AccuKnox AI/ML Assignment – Problem Statement 1
Candidate Details

Name: Jatavath Arjun Kumar
Degree: B.Tech – Civil Engineering
Institute: NIT Warangal

Overview

This repository contains my solution for Problem Statement 1 of the AccuKnox AI/ML assignment.

The objective of this assignment is to demonstrate my ability to:

Work with external data sources (APIs and CSV files)

Store structured data using SQLite

Perform basic data validation and processing

Visualize data for quick analytical insights

Write clean, readable, and explainable Python code

The solution follows a data-first approach, ensuring that data ingestion, validation, and storage layers are stable and reliable before introducing advanced AI/ML models.

Problem Statement Summary

The assignment consists of three independent tasks:

Fetch data from an external REST API and store it in a SQLite database

Import structured data from a CSV file into a SQLite database

Process student score data and visualize insights using a bar chart

Each task is implemented as a separate Python script to maintain clarity, modularity, and ease of testing.

Project Structure
AccuKnox_AI_ML_Assignment
│
├── Problem_Statement_1_Code
│   ├── api_books_to_sqlite.py
│   ├── csv_to_sqlite.py
│   ├── student_scores_visualization.py
│   └── README.md
│
├── data
│   └── user.csv
│
├── database
│   └── accknox.db
│
├── Assignment_Document
│   └── Accuknox_Assignment.docx
│
├── Resume
│   └── Arjun_Resume.pdf

Detailed Implementation Explanation
1. API Data Retrieval and Storage

File: api_books_to_sqlite.py

Functionality:

Attempts to fetch book data from an external REST API

Handles API failures gracefully using exception handling

Uses fallback sample data when the API is unavailable

Stores validated data (title, author, publication year) into a SQLite database

Prevents duplicate entries using database-level constraints

Design Rationale:

External APIs can be unreliable; fallback logic ensures pipeline stability

SQLite is lightweight and sufficient for small to medium datasets

Clear separation between API logic, validation, and database operations improves readability and maintainability

2. CSV Data Import into SQLite

File: csv_to_sqlite.py

Functionality:

Reads user data from a CSV file

Validates required columns and data formats

Creates a users table with appropriate constraints

Inserts valid records into SQLite

Skips duplicate and invalid records safely

Performs basic analytical insight on email domains

Design Rationale:

CSV-to-database ingestion is a common real-world ETL use case

Database constraints improve data integrity

Validation and logging ensure robustness against malformed input

3. Data Processing and Visualization

File: student_scores_visualization.py

Functionality:

Uses simulated student score data

Validates records and handles edge cases

Computes basic statistical metrics (mean, min, max, standard deviation)

Performs simple rule-based classification (pass/fail)

Visualizes scores using a bar chart with an average reference line

Saves the chart as an image file for output verification

Design Rationale:

Visualization helps quickly interpret student performance

Rule-based classification demonstrates ML-ready thinking

Statistical analysis forms a foundation for future predictive modeling

Assumptions

External APIs may be unavailable; fallback data is acceptable

SQLite is sufficient for demonstrating database logic

Dataset size is small to moderate

No authentication is required for the APIs

Focus is on correctness, robustness, and explainability rather than production-scale optimization

How to Run the Code
Step 1: Install Dependencies
pip install -r requirements.txt

Step 2: Run API to SQLite Script
python Problem_Statement_1_Code/api_books_to_sqlite.py

Step 3: Run CSV to SQLite Script
python Problem_Statement_1_Code/csv_to_sqlite.py

Step 4: Run Data Processing and Visualization Script
python Problem_Statement_1_Code/student_scores_visualization.py

Technologies Used

Python

SQLite

Requests

Matplotlib

Possible Improvements and Next Steps

If this system were extended further, I would:

Add structured logging and monitoring for production readiness

Implement retry mechanisms and backoff strategies for API failures

Perform feature engineering on collected data (temporal trends, domain-based grouping)

Apply supervised or unsupervised machine learning models once sufficient labeled data is available

Use the current pipeline as a reliable data ingestion layer for downstream AI/ML systems

Final Note

This assignment reflects my current understanding of Python-based data pipelines and foundational analytics.
I focused on building clean, stable, and explainable data workflows, while intentionally leaving scope for future AI/ML enhancements once the data foundation is validated.
