# Create a set of quiz questions along with their correct answers
quiz = {
    "What is the capital of France?": "Paris",
    "What is the capital of Germany?": "Berlin",
    "What is the capital of Italy?": "Rome",
    "What is the capital of Spain?": "Madrid",
    "What is the capital of Portugal?": "Lisbon",
    "What is the capital of Belgium?": "Brussels",
    "What is the capital of the Netherlands?": "Amsterdam",
    "What is the capital of Austria?": "Vienna",
    "What is the capital of Switzerland?": "Bern",
    "What is the capital of Poland?": "Warsaw",
}

# Greet the player and introduce the quiz
print("Welcome to the European Capitals Quiz!")
print("Answer the questions to the best of your ability. Let's see how much you know!\n")

# Initialize the player's score to zero
score = 0

# Iterate through each question-answer pair in the quiz
for question, answer in quiz.items():
    # Prompt the player for their response and remove any extra spaces
    user_answer = input(question + " ").strip()
    # Check if the player's answer matches the correct one, ignoring case
    if user_answer.lower() == answer.lower():
        print("That's correct!\n")
        score += 1  # Increase the score for a correct response
    else:
        print(f"Oops, the correct answer is {answer}.\n")

# Display the player's final score after completing the quiz
print(f"Quiz complete! You scored {score} out of {len(quiz)}.")