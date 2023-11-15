"""Practicing with Classes."""
from __future__ import annotations

__author__ = "730596810"


class Point:
    """Creating a point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0, y_init: float = 0):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def __str__(self) -> str:
        """Returns point as string."""
        string: str = f"x: {self.x}; y: {self.y}"
        return string
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplies Point by factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point

    def __add__(self, factor: int | float) -> Point:
        """Adds factor to Point."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point  
    
    def scale_by(self, factor: int) -> None:
        """Mutate class point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Create new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point  