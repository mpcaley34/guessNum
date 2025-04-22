

def get_valid_int(prompt, min_val, max_val):

    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(
                    f'Please enter a number between {min_val} and {max_val}.')
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def print_banner(text):
    border = '=' * (len(text) + 4)
    print(f'\n{border}')
    print(f'| {text} |')
    print(f'{border}\n')
