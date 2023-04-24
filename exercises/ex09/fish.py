"""File to define Fish class."""

__author__ = "730568890"


class Fish:
    """Class Fish."""

    age: int
    
    def __init__(self) -> None:
        """Self function."""
        self.age: int = 0
        return None
    
    def one_day(self) -> None:
        """Adds an age."""
        self.age += 1
        return None