from flask import Flask, jsonify, request
from gleam import QuizGenerator, DifficultyManager, StorageHandler

app = Flask(__name__)
qg = QuizGenerator()
dm = DifficultyManager()
sh = StorageHandler()

@app.route("/api/generateQuiz")
def api_generate_quiz():
    topic = request.args.get("topic", "logic")
    user_id = request.args.get("user_id", "anon")

    stats = sh.get_score(user_id)
    user_score = stats['score'] if stats else 0
    difficulty = dm.get_next_level(user_score)
    quiz = qg.generate_question(topic, difficulty)

    return jsonify({
        "question": quiz["question"],
        "options": quiz["options"],
        "difficulty": difficulty
    })

if __name__ == "__main__":
    app.run(port=5000)