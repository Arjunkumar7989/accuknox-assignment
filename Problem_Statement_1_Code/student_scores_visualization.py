import matplotlib.pyplot as plt

# ---------------------------------
# ASSUMPTION:
# Student score data is fetched from an API.
# For this assignment, the data is simulated.
# ---------------------------------

def main():
    students = [
        {"name": "A", "score": 78},
        {"name": "B", "score": 85},
        {"name": "C", "score": 69},
        {"name": "D", "score": 92}
    ]

    # Extract names and scores
    names = [s["name"] for s in students]
    scores = [s["score"] for s in students]

    # Basic analysis
    average_score = sum(scores) / len(scores)
    min_score = min(scores)
    max_score = max(scores)

    print(f"Average Score: {average_score}")
    print(f"Minimum Score: {min_score}")
    print(f"Maximum Score: {max_score}")

    # Visualization
    plt.bar(names, scores)
    plt.axhline(y=average_score, linestyle="--")
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.title("Student Test Scores")

    # Save chart as output proof
    plt.savefig("student_scores.png")
    plt.show()


if __name__ == "__main__":
    main()
