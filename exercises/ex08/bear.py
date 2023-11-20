"""File to define Bear class."""


class Bear:
    """Bear with age and hunger_score."""
    age: int
    hunger_score: int

    def __init__(self):
        """Initializes a new object in bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Adjusts age and hunger_score."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Adjusts hunger based on eating."""
        self.hunger_score += num_fish