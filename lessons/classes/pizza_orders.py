"""Instantiating a class."""

"""
this is where we instantiate the class we defined
in classes.py
aka, were creating objects that belong to the class"""

#import
from lessons.classes.pizza import Pizza

#instantiating pizza:
my_pizza: Pizza = Pizza("Large", True, 10)

#setting attributes

#my_pizza.size = "large"
#my_pizza.gluten_free = True
#my_pizza.toppings = 10 

# to print attribute

#print("size attribute:")
#print(my_pizza.size)

print("Pizza:")
print(Pizza)

#sals_pizza size medium 5 toppings not gf

sals_pizza: Pizza = Pizza("medium", False, 5)

def price(input_pizza: Pizza) -> float:
    """Function to Calculate price of pizza."""
    if input_pizza == "large":
        price: float = 6.25
    else:
        price: float = 5
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00
    return price

#calling function
print(price(sals_pizza))
print(price(my_pizza))
#calling price method
print(sals_pizza.price())
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza.toppings)