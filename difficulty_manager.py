# Simple adaptive difficulty based on score:
# GLEAM/difficulty_manager.py
class DifficultyManager:
    def get_next_level(self, current_score):
        if current_score < 3:
            return "easy"
        elif current_score < 7:
            return "medium"
        else:
            return "hard"
