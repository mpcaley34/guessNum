from game import select_difficulty, play_round
from utils import print_banner


def main():
    print_banner("🎯 Initializing Game... 🎯")

    while True:
        settings = select_difficulty()
        won, score = play_round(settings)

        play_again = input(
            'Do you want to play again? (y/n): ').strip().lower()
        if play_again != 'y':
            print_banner('Thanks for playing!')
            break


if __name__ == '__main__':
    main()
