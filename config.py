class Settings:
    # LLM model name for question generation
    QUESTION_GEN_MODEL = "gpt2"
    # DB path for StorageHandler
    DB_PATH = "gleam.db"
    # Max question length for LLM generation
    MAX_QUESTION_LENGTH = 150
    # Difficulty Levels
    DIFFICULTY_LEVELS = ("easy", "medium", "hard")

settings = Settings()