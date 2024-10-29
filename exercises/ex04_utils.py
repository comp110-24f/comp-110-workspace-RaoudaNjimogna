"""Practiing Computational Thinking"""

__author__: str = "730670839"


def all(list_int: list[int], inter: int) -> bool:
    """This will see is the interger is the same list as int"""
    index: int = 0
    while index < len(list_int):  # this will make sure that the program end
        # runs within the length of our code
        if inter != list_int[index]:
            return False
        else:
            index += 1
    if len(list_int) == 0:
        return False
    return True  # this will run throught the entire list, and
    # will return true is the numbers matched the indicated number


print(all([1, 2, 3], 1))


def max(list_int: list[int]) -> int:
    """This is will return the largest number in the list"""
    if len(list_int) == 0:
        raise ValueError("max() arg is an empty List")
    largest = list_int[0]  # this will initialize the largest number with
    # the first value in the list
    for num in list_int:
        if num > largest:
            largest = (
                num  # if the number is greater than the largest number in the list,
            )
            # it replaces that in this local variable and returns it
    return largest


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """If both the elements in the list are true, it will return true"""
    index = 0
    if len(list_one) < len(list_two):
        if list_one[index] != list_two[index]:
            return False  # if the length of one of the list greater than the second
        # and then it will return false is the lists are not equal, true if they are
        else:
            index += 1
    return True


print(is_equal([1, 1, 0], [1, 0, 1]))


def extend(list_one: list[int], list_two: list[int]) -> None:
    """This will append two lists into just one."""
    for num in list_two:
        list_one.append(
            num
        )  # this will mutate the first list in and appends the second lists to it
