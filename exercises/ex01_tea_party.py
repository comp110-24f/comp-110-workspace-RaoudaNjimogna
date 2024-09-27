"""First exercise of COMP 110"""

__author__: str = "730670839"


def tea_bags(people: int) -> int:
    """Defining a function to compute
    number of tea bags by guest"""

    return people * 2  # Since each guest drinks two drinks, multiplication is needed


def treats(people: int) -> int:
    """Defining a function to compute
    number of treats by number of drinking tea guest"""

    return int((tea_bags(people=people)) * 1.5)
    # Same thought process as before, however took some
    # time to realize that I needed to change data type to int by parenthesis


def cost(tea_count: int, treat_count: int) -> float:
    """Defining a function to compute
    total cost of tea bags and treat"""

    return (tea_count * 0.5) + (treat_count * 0.75)  # Pretty straightforward


def main_planner(guest: int) -> None:
    """Defining a function to print out
    values of each function"""

    print("A Cozy Tea Party for " + str(guest) + " people!")
    print("Tea Bags: " + str(tea_bags(people=guest)))
    print("Treats: " + str(treats(people=guest)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guest), treat_count=treats(guest))))
    # Last print call was confusing due to the fact that I wasn't sure what to
    # substitue the parameters with.


if __name__ == "__main__":
    main_planner(guest=int(input("How many guest are attending you tea party? ")))
"""Asking the users the total amount of the guest attending their party"""
