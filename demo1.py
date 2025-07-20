from gleam import (
    QuizGenerator, DifficultyManager,
    FeedbackEngine, StorageHandler
)

def run_demo():
    user_id = "user123"
    topic = "logic"
    user_score = 4  # example current score

    # Initialize core components
    qg = QuizGenerator()
    dm = DifficultyManager()
    fe = FeedbackEngine()
    sh = StorageHandler()

    # Determine adaptive difficulty level
    difficulty = dm.get_next_level(user_score)
    print(f"Selected difficulty: {difficulty}")

    # Generate a quiz question
    quiz = qg.generate_question(topic, difficulty)
    print("Question:", quiz['question'])
    for key, val in quiz['options'].items():
        print(f"{key}: {val}")

    # Simulate user answer (for demo, choose random option)
    import random
    user_choice = random.choice(list(quiz['options'].keys()))
    print(f"User choice: {user_choice}")

    # Provide feedback
    feedback = fe.explain_answer(quiz['question'], user_choice, quiz['correct_answer'], quiz['explanation'])
    print("Feedback:", feedback)

    # Save the score - let's say user got 1 point if correct, else 0
    score_delta = 1 if user_choice == quiz['correct_answer'] else 0
    current_stats = sh.get_score(user_id) or {'score': 0, 'streak': 0}

    new_score = current_stats['score'] + score_delta
    new_streak = current_stats['streak'] + 1 if score_delta == 1 else 0

    sh.save_score(user_id, new_score, new_streak)
    print(f"Saved new score {new_score} with streak {new_streak} for user {user_id}")

if __name__ == "__main__":
    run_demo()