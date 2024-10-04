"""Making my own Wordle Game!"""

__author__: str = "730670839"

WHITE_BOX: str = "\U00002B1C"  # ⬜
GREEN_BOX: str = "\U0001F7E9"  # 🟩
YELLOW_BOX: str = "\U0001F7E8"  # 🟨


def input_guess(secret_word_len: int) -> str:
    """This will ask the user to guess a word anc check if it's the right length."""
    user_guess = input(f"Enter a {secret_word_len} character word: ")
    while len(user_guess) != secret_word_len:
        user_guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # This will ask the user to enter a new guess if not sufficent,
        # replacing the old guess.
    return user_guess


def contains_char(search_word: str, char_to_find: str) -> bool:
    """Will see if a character that is guess is found within the secret word"""
    assert len(char_to_find) == 1
    index = 0

    while index <= len(search_word) - 1:
        if search_word[index] == char_to_find:
            # If the character is found within the word at that position, it's true
            return True
        else:  # if not, it'll move to the next position and check
            index += 1
    return False  # until it's not found


def emojified(guess_word: str, secret: str) -> str:
    """Will display a string of emojis to show if the characters are in the right place."""
    assert len(secret) == len(guess_word)

    emoji_displayed = ""
    emoji_index = 0

    while emoji_index <= len(guess_word) - 1:
        if (
            guess_word[emoji_index] == secret[emoji_index]
        ):  # the emoji is in the correct position
            emoji_displayed += GREEN_BOX
            emoji_index += 1
        elif contains_char(secret, guess_word[emoji_index]):
            # using the contain_chars function, we can check to see the locations
            # of the character within the guess, and then display an yellow box
            emoji_displayed += YELLOW_BOX
            emoji_index += 1
        else:
            emoji_displayed += WHITE_BOX  # it is not found
            emoji_index += 1
    return emoji_displayed  # shows the position via emojis


def main(secret_word: str) -> None:
    turn_number = 1  # the initial try, will increase each guess
    correct_guess = False  # we start off with the user not yet guessing the word.

    while not correct_guess and turn_number < 7:  # in 6 trys or less
        print(f"=== Turn {turn_number}/6 ===")
        current_guess = input_guess(
            len(secret_word)
        )  # set the required length of guessed words
        print(
            emojified(current_guess, secret_word)
        )  # allows the emojis to diasplay, in correspondance to valid guess
        if current_guess == secret_word:
            print(f"You won in {(turn_number)}/6 turns!")
            correct_guess = True  # user has now won the game
            exit
        turn_number += 1
    if not correct_guess:  # user has used all 6 turns and lost.
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
