"""File to define River class."""
__author__ = "730596810"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """"Class with changes to fish and bears."""

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes certain aged fish and bears."""
        alive_fish: list[Fish] = []
        alive_bears: list[Bear] = []
    
        for animal in self.fish:
            if animal.age <= 3:
                alive_fish.append(animal)
    
        for animal in self.bears:
            if animal.age <= 5:
                alive_bears.append(animal)
            
        self.fish = alive_fish
        self.bears = alive_bears
        return None

    def bears_eating(self):
        """Removes fish and increases bears."""
        for bear in self.bears:
            if len(self.fish) >= 1:
                bear.eat(1)
                if self.fish:
                    self.fish.pop(0)
        return None
    
    def check_hunger(self):
        """Removes bears that die of starvation."""
        full_bears: list[Bear] = []

        for bear in self.bears:
            if bear.hunger_score >= 0:
                full_bears.append(bear)
        self.bears = full_bears
        return None
        
    def repopulate_fish(self):
        """Creates 4 offspring per pair of fish."""
        num_offspring: int = ((len(self.fish) // 2) * 4)
    
        self.fish.extend([Fish() for _ in range(num_offspring)])
    
    def repopulate_bears(self):
        """Creates 1 offspring per pair of bears."""
        num_offspring: int = (len(self.bears) // 2)

        self.bears.extend([Bear() for _ in range(num_offspring)])
    
    def view_river(self):
        """Prints the fish and bears in river."""
        info: str = f"Day {self.day}:\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}"
        print(info)
        return None
            
    def one_river_day(self):
        """Simulate one day in river."""
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
    
    def one_river_week(self):
        """Simulates 7 days."""
        for day in range(7):
            self.one_river_day()
    
    def remove_fish(self, number: int):
        """Remove number of fish."""
        x: int = 0
        while number > x:
            number -= 1
            self.fish.pop(0)
        return None



            
