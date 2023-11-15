"""Defining a class."""
from __future__ import annotations

""" 
Classes are like a roadmap for objects that
belong to that class
we are defining the underlying structure that
every instance this class will have
"""
class Pizza:
    size: str
    toppings: int
    gluten_free: bool

#how to set attributes by putting their value as an argument
#__init__ stays the same for all classes
#this is a constructor
    def __intit__(self, inp_size: str, inp_gf: bool, inp_toppings: int ):
        #self is invisible, basically refers to Pizza
        """My constructor."""
        self.size = inp_size
        self.gluten_free = inp_gf
        self.toppings = inp_toppings
        #return a Pizza object, but don't have to call return 


    def price(self) -> float:
        """Method to Calculate price of pizza."""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    

    def add_toppings(self, num_toppings: int) -> Pizza:
        """Add toppings to existing pizza"""
        self.toppings += num_toppings

        
    def make_new_pizza_add_toppings(self, num_toppings: int):
        """Make a new pizza w existing properties and add toppings"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
    def __str__(self) -> str:
        pizza_info: str = f"PIZZA ORDER: size: {self.size}, toppings: {self.toppings}, GF: {self.gluten_free}"
        return pizza_info

my_pizza: Pizza = Pizza("medium", 3, False)
print(str(my_pizza))