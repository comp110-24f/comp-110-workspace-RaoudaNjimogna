"""Defining Unit Tests for Lists Utilities"""

__author__: str = "730670839"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_evens_list():
    """this is a use case, testing to see if we can just develop a list with just evens"""
    test_list = [2, 5, 6, 7, 10]
    assert only_evens(test_list) == [2, 6, 10]  # this should be the result


def test_no_evens():
    """this is a use case, testing if presented with no evens, an empty list will display"""
    test_list = [1, 3, 5, 7, 9]
    assert only_evens(test_list) == []
    assert test_list == [1, 3, 5, 7, 9]  # makes sure that the list isn't mutated


def test_empty_evens_list():
    """this is an edge case, testing what happens when the list is empty"""
    test_list = []
    assert only_evens(test_list) == []  # this should return sand empty list


def test_unmutated_sublist():
    """this is an use case, testing if an empty list will be returned when given
    out of bounds ranges"""
    test_list = [10, 11, 12, 13, 14, 16]
    assert sub(test_list, 7, -1) == []  # this should be what is returned
    assert test_list == [
        10,
        11,
        12,
        13,
        14,
        16,
    ]  # the test list should remain unchanged/unmutated


def test_sub():
    """This is a use case test, and it will check to see if the sub function works"""
    test_list = [5, 10, 15, 20]
    assert sub(test_list, 1, 3) == [10, 15]
    assert test_list == [5, 10, 15, 20]  # the list itself shouldn't change


def test_empty_sublist():
    """this is an edge case that should return an empty list if list given is empty"""
    test_list = []
    assert sub(test_list, 0, 1) == []


def test_mutate_add_at_index():
    """another use case that will mutate the test list"""
    test_list = [2, 5, 8, 10, 12]
    add_at_index(test_list, 4, 3)
    assert test_list == [
        2,
        5,
        8,
        4,
        10,
        12,
    ]  # this will put the element 4 in the 3 position of the list'


def test_add_at_indexerror():
    """this is an edge case: adding at an index out of range should raise IndexError."""
    input_list = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(input_list, 4, 5)  # an invalid index should raise the IndexError


def test_add_at_index_middle():
    """this is a use case test that adds an element at the middle index of the list."""
    test_list = [1, 2, 4, 5]
    add_at_index(test_list, 3, 2)
    assert test_list == [1, 2, 3, 4, 5]  # this is the result


if __name__ == "__main__":
    test_evens_list()
    test_no_evens()
    test_empty_evens_list()
    test_unmutated_sublist()
    test_sub()
    test_empty_sublist()
    test_mutate_add_at_index()
    test_add_at_indexerror()
    test_add_at_index_middle()
