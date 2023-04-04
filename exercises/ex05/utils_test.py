"""ex05 - Utils Test."""

__author__ = "730566890"

from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Edge case - empty!"""
    assert only_evens([]) == []


def test_only_evens_0() -> None:
    """Use case - positive integers!"""
    test_list: list[int] = [4, 5, 6]
    assert only_evens(test_list) == [4, 6]


def test_only_events_1() -> None:
    """Use case - negative integers!"""
    test_list: list[int] = [-1, -2, -3, -4, -5, -6, -7]
    assert only_evens(test_list) == [-2, -4, -6]


def test_concat_empty() -> None:
    """Edge case with concat!"""
    assert concat([], []) == []


def test_concat_0() -> None:
    """Use case - positive numbers!"""
    x: list[int] = [1, 6, 8]
    y: list[int] = [4, 53, 2]
    assert concat(x, y) == [1, 6, 8, 4, 53, 2]


def test_concat_1() -> None:
    """Use case - negative numbers!"""
    x: list[int] = [-3, 4, -11, 0]
    y: list[int] = [-2, -2, -2]
    assert concat(x, y) == [-3, 4, -11, 0, -2, -2, -2]


def test_sub_empty() -> None:
    """Edge case with sub!"""
    a: list[int] = []
    assert sub(a, 0, 0) == []


def test_sub_0() -> None:
    """Use case with positive numbers!"""
    a: list[int] = [50, 60, 30, 12]
    assert sub(a, 2, 4) == [30, 12]


def test_sub_1() -> None:
    """Test where start index is negative!"""
    a: list[int] = [22, 11, 60, 40, 20]
    assert sub(a, -1, 4) == [22, 11, 60, 40]
