# Exercise 4: Primitive Quiz (Advanced)

# Step 1: Create a dictionary of questions and answers
quiz = {
    "What is the capital of France? ": "paris",
    "What is the capital of Germany? ": "berlin",
    "What is the capital of Italy? ": "rome",
    "What is the capital of Spain? ": "madrid",
    "What is the capital of Portugal? ": "lisbon",
    "What is the capital of Greece? ": "athens",
    "What is the capital of Austria? ": "vienna",
    "What is the capital of Belgium? ": "brussels",
    "What is the capital of Netherlands? ": "amsterdam",
    "What is the capital of Switzerland? ": "bern"
}

# Step 2: Initialize score
score = 0

# Step 3: Loop through questions
for question, correct_answer in quiz.items():
    answer = input(question)
    # Ignore capitalization
    if answer.lower().strip() == correct_answer:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! The correct answer is:", correct_answer.capitalize())
    print()

# Step 4: Final result
print("You got", score, "out of", len(quiz), "correct!")
