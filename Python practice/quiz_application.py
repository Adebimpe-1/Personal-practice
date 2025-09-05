questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
    {"question": "2 + 2 equals?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "Python is a ___?", "options": ["Snake", "Programming Language", "Car"], "answer": "Programming Language"}
]

def run_quiz():
    score = 0
    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        choice = int(input("Your answer (number): "))
        if q["options"][choice - 1] == q["answer"]:
            score += 1
    print(f"Your score: {score}/{len(questions)}")

run_quiz()

