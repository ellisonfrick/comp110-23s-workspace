"""Odd and Even"""

def odd_and_even(x: list[int]) -> list[int]:
    """Return list containing elements that are odd and have even index"""
    idx: int = 0
    list: list[int] = []

    while idx < len(x):
        if x % 2 == 1 and idx % 2 == 0:
            list.append(x[idx])
    idx += 1

    return list

print(odd_and_even(7,8,10,5,3))