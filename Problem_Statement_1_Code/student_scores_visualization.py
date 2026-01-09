import matplotlib.pyplot as plt
import logging
from statistics import mean, stdev
from typing import List, Dict

# ---------------------------------
# CONFIGURATION
# ---------------------------------
OUTPUT_IMAGE = "student_scores.png"
PASS_MARK = 75
LOG_FILE = "student_analysis.log"

# ---------------------------------
# LOGGING SETUP
# ---------------------------------
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ---------------------------------
# DATA VALIDATION
# ---------------------------------
def validate_students(students: List[Dict]) -> List[Dict]:
    valid_students = []

    for s in students:
        if (
            isinstance(s, dict) and
            isinstance(s.get("name"), str) and s["name"].strip() != "" and
            isinstance(s.get("score"), (int, float)) and 0 <= s["score"] <= 100
        ):
            valid_students.append(s)
        else:
            logging.warning(f"Invalid record skipped: {s}")

    return valid_students

# ---------------------------------
# BASIC ML / ANALYTICS LAYER
# ---------------------------------
def analyze_scores(scores: List[float]) -> None:
    avg = mean(scores)
    minimum = min(scores)
    maximum = max(scores)
    deviation = round(stdev(scores), 2) if len(scores) > 1 else 0

    print(f"📊 Average Score: {avg}")
    print(f"⬇️ Minimum Score: {minimum}")
    print(f"⬆️ Maximum Score: {maximum}")
    print(f"📈 Standard Deviation: {deviation}")

    logging.info(
        f"Stats | Avg: {avg}, Min: {minimum}, Max: {maximum}, StdDev: {deviation}"
    )

# ---------------------------------
# SIMPLE AI CLASSIFICATION
# ---------------------------------
def classify_students(students: List[Dict]) -> None:
    passed = [s["name"] for s in students if s["score"] >= PASS_MARK]
    failed = [s["name"] for s in students if s["score"] < PASS_MARK]

    print(f"✅ Passed Students: {passed}")
    print(f"❌ Failed Students: {failed}")

    logging.info(f"Passed: {passed}, Failed: {failed}")

# ---------------------------------
# VISUALIZATION
# ---------------------------------
def plot_scores(names: List[str], scores: List[float], avg_score: float) -> None:
    try:
        plt.figure()
        plt.bar(names, scores)
        plt.axhline(y=avg_score, linestyle="--")
        plt.xlabel("Students")
        plt.ylabel("Scores")
        plt.title("Student Test Scores")

        plt.savefig(OUTPUT_IMAGE)
        plt.close()

        logging.info("Score chart saved successfully")

    except Exception as e:
        logging.error(f"Plotting failed: {e}")
        print("❌ Error occurred while creating the chart.")

# ---------------------------------
# MAIN PIPELINE
# ---------------------------------
def main() -> None:
    try:
        # Assumed API response (simulated)
        students = [
            {"name": "A", "score": 78},
            {"name": "B", "score": 85},
            {"name": "C", "score": 69},
            {"name": "D", "score": 92}
        ]

        students = validate_students(students)

        if not students:
            raise ValueError("No valid student records available")

        names = [s["name"] for s in students]
        scores = [s["score"] for s in students]

        analyze_scores(scores)
        classify_students(students)

        avg_score = mean(scores)
        plot_scores(names, scores, avg_score)

        print("✅ Student score analysis completed")

    except ValueError as ve:
        logging.critical(ve)
        print(f"❌ {ve}")

    except Exception as e:
        logging.critical(f"Unexpected failure: {e}")
        print("❌ Unexpected error occurred. Check logs.")

# ---------------------------------
# ENTRY POINT
# ---------------------------------
if __name__ == "__main__":
    main()
