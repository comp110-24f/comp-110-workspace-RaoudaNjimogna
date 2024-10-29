"""Implementing List Utility Functions """

__author__: str = "730670839"


def only_evens(find_evens: list[int]) -> list[int]:
    evens = []  # this will create an empty list to store the even values

    for num in find_evens:  # this will loop over the find_evens list
        if num % 2 == 0:  # searching for whether each number is divisible by 2 (even)
            evens.append(num)
    return evens  # numbers that pass the test, add to evens list


def sub(top_list: list[int], start_index: int, end_index: int) -> list[int]:
    subset = []  # creates empty list for later subsetted liste

    if len(top_list) == 0 or start_index >= len(top_list) or end_index <= 0:
        return (
            []
        )  # this will generate an empty list the inputed values are out of range
    if start_index < 0:  # sets the start index to be in bounds
        start_index = 0
    if end_index > len(top_list):  # same for end
        end_index = len(top_list)

    index = start_index  # we will go over each element of the list that is
    # within the constraints of our set index ranges
    while index < end_index:
        subset.append(top_list[index])  # this will add them to the subset list.
        index += 1
    return subset


def add_at_index(main_list: list[int], element: int, placement: int) -> None:
    if placement < 0 or placement > len(
        main_list
    ):  # this checks if the index is out of range and will raise an IndexError if it is.
        raise IndexError("Index is out of bounds for the input list")
    # this will append a placeholder to the end of the list to create space
    main_list.append(0)  # thus making the list one element longer.

    index = len(main_list) - 2  # this wills start shifting from the second last element
    while index >= placement:
        main_list[index + 1] = main_list[index]  # index to index + 1
        index -= 1

    main_list[placement] = element  # inserts new element at the given placement
