# AccuKnox AI/ML Assignment – Submission

## Candidate Information
Name: Jatavath Arjun Kumar  
Degree: B.Tech – Civil Engineering  
Institute: NIT Warangal  

---

## Purpose of This Assignment
This repository is my submission for the AccuKnox AI/ML assignment.

The purpose of this assignment is to demonstrate:
- Basic Python programming skills
- Handling data from APIs and CSV files
- Storing data in a SQLite database
- Performing simple data processing
- Visualizing data using Python

I have focused on keeping the implementation **simple, correct, and easy to understand**, exactly as required by the problem statement.

---

## Project Structure Explained
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

Each folder has a specific purpose:
- **Problem_Statement_1_Code**: All Python scripts related to the assignment
- **data**: Input CSV file used for database insertion
- **databse**: SQLite database file created by the scripts
- **Assignment_Document**: Written explanation and theory answers
- **GitHub_Links**: Links to my complex Python and database projects
- **Resume**: Latest resume

---

## Step-by-Step Explanation of the Code

### Step 1: API Data Retrieval and Storage
**File:** `api_books_to_sqlite.py`

What this script does:
1. Tries to fetch book data from an external REST API using Python.
2. If the API is not reachable, the script uses predefined sample data.
3. Creates a SQLite database (if it does not already exist).
4. Creates a table to store book details.
5. Inserts book data (title, author, publication year) into the database.

Why this step is important:
- Shows how external data can be collected
- Demonstrates basic API handling and database storage

---

### Step 2: CSV Data Import into SQLite
**File:** `csv_to_sqlite.py`

What this script does:
1. Reads user data from a CSV file (`user.csv`).
2. Connects to the SQLite database.
3. Creates a table for user information.
4. Inserts each row from the CSV file into the database.

Why this step is important:
- CSV to database ingestion is a very common real-world task
- Demonstrates file handling and database insertion logic

---

### Step 3: Data Processing and Visualization
**File:** `student_scores_visualization.py`

What this script does:
1. Fetches student score data (simulated API source).
2. Calculates the average score.
3. Creates a bar chart showing individual student scores.
4. Displays or saves the chart for visual analysis.

Why a bar chart was used:
- It allows easy comparison between students
- It clearly shows differences in scores

---

## Assumptions Made
- API responses are in a consistent JSON format
- SQLite is sufficient for local storage
- Data size is small to moderate
- No API authentication is required
- Focus is on correctness rather than large-scale optimization

---

## How to Run This Project (Very Important)

### Step 1: Install Python
Ensure Python 3.x is installed on your system.

### Step 2: Install Required Libraries
Open terminal or command prompt in the project folder and run:
pip install -r requirements.txt

graphql
Copy code

### Step 3: Run API to Database Script
python Problem_Statement_1_Code/api_books_to_sqlite.py

pgsql
Copy code
This will create the database and insert book data.

### Step 4: Run CSV to Database Script
python Problem_Statement_1_Code/csv_to_sqlite.py

pgsql
Copy code
This will insert user data from the CSV file into the database.

### Step 5: Run Data Processing and Visualization Script
python Problem_Statement_1_Code/student_scores_visualization.py

yaml
Copy code
This will calculate the average score and display the bar chart.

---

## Technologies Used
- Python
- SQLite
- Requests
- Pandas
- Matplotlib

---

## Final Note
This assignment reflects my current level of understanding of Python, data handling, and basic data analysis.  
I am continuously improving my skills in AI/ML concepts alongside practical implementation.

---

End of submission.
