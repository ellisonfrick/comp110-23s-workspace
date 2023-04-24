"""File to define Bear class."""

__author__ = "730568890"


class Bear:
    """Class Bear."""   

    age: int
    hunger_score: int 

    def __init__(self) -> None:  # Self function
        """Self function."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None
    
    def one_day(self) -> None:
        """Ages one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Adds num_fish to hunger."""
        self.hunger_score += num_fish
        return None