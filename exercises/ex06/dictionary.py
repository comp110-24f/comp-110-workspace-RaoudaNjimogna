"""Practice with Dictionary Functions"""

__author__: str = "730670839"


def invert(key_invert: dict[str, str]) -> dict[str, str]:
    invert_dict = {}
    # this empty dictionary will store the inverted key and value pairs
    for key in key_invert:
        # will loop thru each key in the dictionary and get their respective value
        value = key_invert[key]
        if (
            value in invert_dict
        ):  # this will check for duplicate keys and raise value if present
            raise KeyError("Duplicate key encountered when inverting dictionary.")
        invert_dict[value] = (
            key  # inverts the key and value pair and assigns it to the new dictionary
        )
    return invert_dict


def favorite_colors(color_names: dict[str, str]) -> str:
    # we will create an empty dictionary to keep track of the frequency of colors
    color_counter = {}

    for name in color_names:
        color = color_names[name]
        if color in color_counter:
            color_counter[color] += 1
        else:
            color_counter[color] = 1  # this will be the colors first/only occurance
        # we will assign the variable color to the values of the names,
        # then we will keep track of their occurances and track them in our empty dictionary

        popular_color = ""  # this will store the most popular color
        popular_color_count = 0  # index
        # in order to find the most popular color, we need interate thru our no longer
        # empty dicitonary and find the color with the highest count
        for color in color_counter:
            if color_counter[color] > popular_color_count:
                popular_color = color
                popular_color_count = color_counter[color]
            # if there is a tie, we will set the color that reaches the max count (appearing first)
            # as the most popular color and then set that into our empty string and return the value
            elif color_counter[color] == popular_color_count and popular_color == "":
                popular_color = color
        return popular_color


def count(count_values: list[str]) -> dict[str, int]:
    dict_values = {}  # setting an empty dictionary to
    # store the count (value) of each element (key) in the list
    for (
        value
    ) in (
        count_values
    ):  # will check to see if the values in the list are a key in the empty
        # dictionary and will increase the count by one if they are.
        if value in dict_values:
            dict_values[value] += 1
        else:
            dict_values[value] = 1  # first and only occurance

    return dict_values


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    dict_words = {}  # creating an empty dictionary to store words
    for word in words:
        letter = word[0].lower()  # changes the first letter of the word lowercase
        if letter not in dict_words:
            dict_words[letter] = (
                list()
            )  # creates a list for words that do not exist in dict
            # so that we won't raise any errors, ensuring that each unique starting
            # letter has its own list of words
        dict_words[letter].append(word)  # adds the word to dictionary
    return dict_words


def update_attendance(
    day_attendance: dict[str, list[str]], day: str, student: str
) -> None:
    if day in day_attendance:  # does day exist in attendence log? if yes
        # add the student to the list
        day_attendance[day].append(student)
    else:  # if day is not in list, then enter a new entry in the dict with
        # with the day as key and the value being a new list containing the
        # student's name.
        day_attendance[day] = [student]
