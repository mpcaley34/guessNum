from config import WELCOME_BANNER, DIFFICULTY_PROMPT, DIFFICULTY_SETTINGS

from utils import print_banner, get_valid_int

import random


def select_difficulty():
    print_banner("🎯 Number Guessing Game 🎯")
    print(WELCOME_BANNER)
    print(DIFFICULTY_PROMPT)

    choice = get_valid_int("Your choice ", 1, 3)
    difficulty_key = str(choice)

    settings = DIFFICULTY_SETTINGS[difficulty_key]
    print(f'You selected: {settings['label']} mode!')
    return settings  # returns dict with min, max, guesses and label


def play_round(settings):
    min_val, max_val, max_guesses, label = settings['min'], settings[
        'max'], settings['guesses'], settings['label']

    secret = random.randint(min_val, max_val)
    attempts = 0
    won = False

    print(f'Starting {label} Mode')
    print(f'You need to guess a number between {min_val} and {max_val}')
    print(f'You have {max_guesses} attempts. Good luck!')

    while attempts < max_guesses:
        guess = get_valid_int(f'Guess #{attempts + 1}: ', min_val, max_val)
        attempts += 1

        if guess == secret:
            print('Correct! You guessed the right number')
            won = True
            break
        elif guess < secret:
            print('Too low!')
        elif guess > secret:
            print('Too high!')

        remaining = max_guesses - attempts
        if remaining:
            print(
                f'You have {remaining} guess{'es' if remaining > 1 else ''} left')
        else:
            print('You ran out of guesses!')
    if not won:
        print(f'Sorry, the number was {secret}')

    # Scoring: bonus for fewer attempts
    score = max(0, 100 - 10 * (attempts - 1)) if won else 0
    print(f'Your score: {score}')

    return won, score


def calculate_score():
    pass
