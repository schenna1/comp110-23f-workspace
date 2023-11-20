"""File to define Fish class."""


class Fish:
    """Class fish with age."""
    age: int
    
    def __init__(self):
        """Initializes fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Adjusts age."""
        self.age += 1
        return None