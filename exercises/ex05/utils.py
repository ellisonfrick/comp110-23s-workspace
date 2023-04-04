"""ex05- Utils."""

__author__ = "730566890"


def only_evens(list1: list[int]) -> list[int]:  # Function that pulls out only even numbers
    """Returns a new list contianing only the elements of the input list that were even!"""
    i: int = 0  # assignes i to 0
    evenslist: list[int] = []
    while i < len(list1):
        if list1[i] % 2 == 0:  # Proves the list index is even
            evenslist.append(list1[i])
        i += 1
    return evenslist


def concat(x: list[int], y: list[int]) -> list[int]:  # Function that adds first list to the second
    """Returns a list containing all elements of first list, followed by the second list!"""
    i: int = 0
    idx: int = 0
    concat: list[int] = []
    while i < len(x):  # Checking i for first list
        concat.append(x[i])
        i += 1
    while idx < len(y):  # Checking i for second list
        concat.append(y[idx])
        idx += 1
    return concat


def sub(a: list[int], b: int, c: int) -> list[int]:  # Function that returns a subset
    """Returns a subset list between start index and end index -1!"""
    if b < 0:  # If first number is negative
        b = 0
    if c > len(a):  # If last number is greater than len of list
        c = len(a)
    if len(a) == 0 or b >= len(a) or c <= 0:
        return []  # Return empty list
    i: int = b
    subset: list[int] = []
    while i < c:
        subset.append(a[i])
        i += 1
    return subset
