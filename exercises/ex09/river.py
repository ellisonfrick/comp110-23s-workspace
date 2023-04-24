"""File to define River class."""

__author__ = "730568890"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Class River."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Removes fishes above age 3 and bears above age 5."""
        new_fish: list = []
        new_bear: list = []
        for idx in self.fish:
            if idx.age <= 3:
                new_fish.append(idx)
        self.fish = new_fish
        for i in self.bears:
            if i.age <= 5:
                new_bear.append(i)
        self.bears = new_bear
        return None

    def remove_fish(self, amount: int) -> None:
        """Remove amount many fish from the river."""
        for i in range(0, amount):
            self.fish.pop(0)
        return None

    def bears_eating(self) -> None:
        """Bears eating each three fish."""
        for i in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                i.eat(3)
        return None
    
    def check_hunger(self) -> None:
        """Remove beawr if its hunger score is lower than 0."""
        new_bear: list[Bear] = []
        for i in self.bears:
            if i.hunger_score >= 0:
                new_bear.append(i)
        self.bears = new_bear
        return None
        
    def repopulate_fish(self) -> None:
        """Each pair of fish produce 4 offspring."""
        offspring_fish: int = (len(self.fish) // 2) * 4
        for i in range(0, offspring_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self) -> None:
        """Each pair of Bear's produce 1 offspring."""
        offspring_bear: int = (len(self.bears) // 2)
        for i in range(0, offspring_bear):
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        """Prints out river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self) -> None:
        """Calls one_river_day seven times."""
        for i in range(0, 7):
            self.one_river_day()
        return None