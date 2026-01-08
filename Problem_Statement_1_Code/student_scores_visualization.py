import matplotlib.pyplot as plt

# Assumption:
# Student scores are fetched from an API (simulated here)

def main():
    students = [
        {"name": "A", "score": 78},
        {"name": "B", "score": 85},
        {"name": "C", "score": 69},
        {"name": "D", "score": 92}
    ]

    names = [s["name"] for s in students]
    scores = [s["score"] for s in students]

    average_score = sum(scores) / len(scores)
    print(f"Average Score: {average_score}")

    plt.bar(names, scores)
    plt.axhline(y=average_score, linestyle="--")
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.title("Student Test Scores")

    plt.show()


if __name__ == "__main__":
    main()
