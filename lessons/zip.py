"""Zip Function!"""

def zip(x: list[str], y: list[int]) -> dict[str,int]:
    """Keys are items of the first list and values the same index of second list"""
    dict1: dict[str,int] = {}
    if len(x) != len(y) or len(x) == 0 or len(y) == 0:
        return dict1
    for idx in range(0, len(x)):
        dict1[x[idx]] = y[idx]
    return dict1
