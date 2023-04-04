"""EX07 - Dictionary Tests!"""

__author__ = "730566890"

from dictionary import invert, count, favorite_color
import pytest


def test_invert_empty() -> None:  # Empty invert
    """Edge case - invert."""
    assert invert({}) == {}


def test_invert_1() -> None:  # Invert with colors
    """Use Case with invert."""
    dictionary1: dict[str, str] = {'green': 'tree', 'pink': 'flower', 'blue': 'sky'}
    new_dict: dict[str, str] = {'tree': 'green', 'flower': 'pink', 'sky': 'blue'}
    assert invert(dictionary1) == new_dict


def test_invert_2() -> None:  # Invert with animals
    """Use case with invert."""
    dictionary1: dict[str, str] = {'dog': 'park', 'cat': 'yarn', 'goat': 'zoo'}
    new_dict: dict[str, str] = {'park': 'dog', 'yarn': 'cat', 'zoo': 'goat'}
    assert invert(dictionary1) == new_dict


with pytest.raises(KeyError):  # Testing keyerror
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_count_empty() -> None:  # Count edge case
    """Edge case - count."""
    assert count([]) == {}


def test_count_1() -> None:  # Testing count with colors
    """Use case with invert."""
    list1: list[str] = ['purple', 'blue', 'purple', 'green']
    list2: dict[str, int] = {'purple': 2, 'blue': 1, 'green': 1}
    assert count(list1) == list2


def test_count_2() -> None:  # testing count with subjects
    """Use case with invert."""
    list1: list[str] = ['math', 'math', 'biology', 'math', 'chemistry']
    list2: dict[str, int] = {'math': 3, 'biology': 1, 'chemistry': 1}
    assert count(list1) == list2


def test_favorite_color_empty() -> None:  # testing favorite color empty
    """Edge case - favorite color."""
    assert favorite_color({}) == ""


def test_favorite_color_1() -> None:  # testing favorite color with names and colors
    """Use case with favorite color."""
    dictionary1: dict[str, str] = {"Ellison": "blue", "Emily": "blue", "Rachel": "red"}
    new_dict: str = "blue"
    assert favorite_color(dictionary1) == new_dict


def test_favorite_color_2() -> None:  # testing favorite colors with letters and colors
    """Use case with favorite color."""
    dictionary1: dict[str, str] = {"A": "blue", "B": "red", "C": "green", "D": "orange", "E": "green"}
    new_dict: str = "green"
    assert favorite_color(dictionary1) == new_dict