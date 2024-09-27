"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730670839"


def input_word() -> str:
    user_input = input("Enter a 5-character word:")
    # This will check if the user inputted word is equal to 5
    if len(user_input) == 5:
        return user_input
    # If not equal, it'll return an error and exit the code
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    user_letter = input("Enter a single character:")
    if len(user_letter) == 1:  # checks length of letter to ensure its 1
        return user_letter
    else:  # same thougt process as input_word
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    letter_count = 0  # will keep track of the instances of the letter in the word.
    print("Searching for " + letter + " in " + word)
    # If word's index matches the letter, then have
    # the letter count increase by one and print it's location.

    # At first I had attempted to use a while loop, however I was
    # stuck in an infinite loop and decided, perhaps
    # just using 6 if statements and an elif to display the letter instance count.
    if word[0] == letter:
        letter_count += 1
        print(letter + " found at index 0")

    if word[1] == letter:
        letter_count += 1
        print(letter + " found at index 1")

    if word[2] == letter:
        letter_count += 1
        print(letter + " found at index 2")

    if word[3] == letter:
        letter_count += 1
        print(letter + " found at index 3")

    if word[4] == letter:
        letter_count += 1
        print(letter + " found at index 4")

    if letter_count == 0:
        print("No instances of " + letter + " found in " + word)

    elif letter_count == 1:
        print(str(letter_count) + " instance of " + letter + " found in " + word)
    # letter_count is still an int, so change the int to str to
    # make displat with this printed string.
    else:
        print(str(letter_count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
