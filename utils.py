import random

def shuffle_choices(options: dict, correct_key: str):
    """
    Shuffle multiple choice options while keeping track of correct key.

    Args:
        options (dict): keys are letters 'A'-'D', values are option text
        correct_key (str): letter of correct answer

    Returns:
        (shuffled_options, new_correct_key)
    """
    items = list(options.items())
    random.shuffle(items)
    new_options = {}
    letters = ['A', 'B', 'C', 'D']

    correct_text = options[correct_key]
    new_correct_key = None

    for idx, (old_key, text) in enumerate(items):
        new_options[letters[idx]] = text
        if text == correct_text:
            new_correct_key = letters[idx]

    return new_options, new_correct_key