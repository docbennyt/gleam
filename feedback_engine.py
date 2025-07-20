# Answer explanation feedback engine:
# GLEAM Feedback Engine
class FeedbackEngine:
    def explain_answer(self, question, user_choice, correct_choice, explanation=None):
        if user_choice == correct_choice:
            return "Correct! You understood the concept well."
        else:
            expl = explanation or "No explanation available."
            return f"Incorrect. The correct answer was {correct_choice} because {expl}"