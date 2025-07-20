from transformers import pipeline
import re
from .config import settings
from .utils import shuffle_choices

class QuizGenerator:
    def __init__(self):
        # Initialize the text generation pipeline only once
        self.generator = pipeline("text-generation", model=settings.QUESTION_GEN_MODEL)

    def generate_question(self, topic, difficulty="medium"):
        if difficulty not in settings.DIFFICULTY_LEVELS:
            difficulty = "medium"
        prompt = f"Generate a {difficulty} level multiple-choice question on {topic} with options (A, B, C, D), correct answer and explanation."
        # Generate text
        result = self.generator(prompt, max_length=settings.MAX_QUESTION_LENGTH, num_return_sequences=1)[0]['generated_text']

        # Parse generated text to structured question
        question = self._parse_generated_text(result)
        # Return a dict with question, options, correct answer, and explanation
        return question

    def _parse_generated_text(self, text):
        """
        Attempts to extract question, options, correct answer and explanation from generated text
        Expected format (approx):
        Q: ...
        A) ...
        B) ...
        C) ...
        D) ...
        Answer: <letter>
        Explanation: ...
        """

        # Extract question
        question_match = re.search(r"(?:Q:|Question:)(.*?)(?:A\)|B\)|C\)|D\))", text, re.DOTALL | re.IGNORECASE)
        question = question_match.group(1).strip() if question_match else "Could not parse question."

        # Extract options
        option_pattern = r"([A-D])\)\s*(.*)"
        options = {}
        for match in re.finditer(option_pattern, text, re.IGNORECASE):
            key = match.group(1).upper()
            value = match.group(2).strip()
            options[key] = value

        # Extract answer (letter)
        answer_match = re.search(r"Answer:\s*([A-D])", text, re.IGNORECASE)
        correct_answer = answer_match.group(1).upper() if answer_match else None

        # Extract explanation
        explanation_match = re.search(r"Explanation:(.*)", text, re.DOTALL | re.IGNORECASE)
        explanation = explanation_match.group(1).strip() if explanation_match else "No explanation provided."

        # If options empty or incomplete, fallback simple split to avoid failure
        if len(options) < 2:
            # Split by lines and heuristically guess options
            options = {}
            lines = text.split('\n')
            opt_letters = ['A', 'B', 'C', 'D']
            idx = 0
            for line in lines:
                line = line.strip()
                if idx >= 4:
                    break
                if line and (line.startswith(opt_letters[idx]) or line.startswith(f"{opt_letters[idx]})")):
                    option_text = line[len(opt_letters[idx])+1:].strip() if line.startswith(opt_letters[idx]) else line[len(opt_letters[idx])+2:].strip()
                    options[opt_letters[idx]] = option_text
                    idx += 1

        # Shuffle options for randomness
        if options and correct_answer:
            options, correct_answer = shuffle_choices(options, correct_answer)

        return {
            "question": question,
            "options": options,
            "correct_answer": correct_answer,
            "explanation": explanation
        }