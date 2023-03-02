"""EX04 - Utility Functions!"""

__author__ = "730566890"


def all(list: list[int], i: int) -> bool:  # Function to see if int is in list given
    """Indicate whether or not all the ints in list are same as given int!"""
    x = 0
    if len(list) == 0:
        return False
    while x < len(list):  
        if list[x] != i:  # Index in list is not equal to integer
            return False
        x += 1
    return True


def max(input: list[int]) -> int:  # Function to see the largest number in the list
    """Max returns the largest in the List!"""
    x: int = 0
    my_max: int = 0
    if len(input) == 0:  # If list is empty
        raise ValueError("max() arg is an empty List")
    while x < len(input):  
        if x == 0:
            my_max = input[x]  # Reassigns my_max
        else:
            if input[x] > my_max:  
                my_max = input[x]
        x += 1
    return my_max
    

def is_equal(x: list[int], y: list[int]) -> bool:  # Function to check if list are the same
    """Checks the length of each List to see is they are equal!"""
    i = 0
    if len(x) != len(y):  # Lists are not the same length
        return False
    while i < len(x):  # Lists do not match
        if x[i] != y[i]:
            return False
        i += 1
    return True  # Lists match
