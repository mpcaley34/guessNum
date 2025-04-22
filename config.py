
DIFFICULTY_SETTINGS = {
    '1': {'label': 'Easy', 'min': 1, 'max': 10, 'guesses': 5},
    '2': {'label': 'Medium', 'min': 1, 'max': 50, 'guesses': 7},
    '3': {'label': 'Hard', 'min': 1, 'max': 100, 'guesses': 10},

}


WELCOME_BANNER = """
🎯 Welcome to the Number Guessing Game!
Try to guess the secret number before you run out of attempts.
"""

DIFFICULTY_PROMPT = """
Choose a difficulty level:
1. Easy (1-10) - 5 guesses
2. Medium (1,50) - 7 guesses
3. Hard (1,100) - 10 guesses

Enter 1, 2, or 3:
"""
