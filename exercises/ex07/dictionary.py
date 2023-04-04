"""EXO7 - Dictionary!"""

__author__ = "730566890"


def invert(list_1: dict[str, str]) -> dict[str, str]:  # Function inverts dictionary
    """Inverts they keys and values."""
    invert_dict: dict[str, str] = {}
    for key in list_1:
        if list_1[key] in invert_dict:
            raise KeyError("Error: There is more than one of the same key.")
        invert_dict[list_1[key]] = key
    return invert_dict 


def count(list_1: list[str]) -> dict[str, int]:  # Function returns key value
    """Return unique key value in given list and each value associated is the count of appearances."""
    empty_dict: dict[str, int] = {}
    for key in list_1:
        if key in empty_dict:
            empty_dict[key] += 1
        else:
            empty_dict[key] = 1
    return empty_dict


def favorite_color(list_1: dict[str, str]) -> str:  # Function finds favorite color
    """Returns color that appears most frequently."""
    new: str = ""
    color: list[str] = []
    favorite = 0
    for key in list_1:
        color.append(list_1[key])
    list_2: dict[str, int] = count(color)
    for key in list_2:
        if favorite < list_2[key]:
            favorite = list_2[key]
            new = key
    return new