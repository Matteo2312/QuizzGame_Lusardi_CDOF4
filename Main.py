def ask_question(question, choices, correct_answer):
    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    user_answer = input("Enter the number of your answer: ")
    return user_answer.strip() == correct_answer

def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "1"
        },
        {
            "question": "What is 2 + 2?",
            "choices": ["3", "4", "5", "6"],
            "correct_answer": "2"
        },
        {
            "question": "What is the square root of 9?",
            "choices": ["3", "4", "2", "6"],
            "correct_answer": "2"
        },
        {
            "question": "How many moons does Jupiter",
            "choices": ["95", "38", "86", "52"],
            "correct_answer": "86"
        },

    ]

    score = 0
    for q in questions:
        if ask_question(q["question"], q["choices"], q["correct_answer"]):
            print("Correct!")
            score += 1
        else:
            print("Wrong answer.")

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
