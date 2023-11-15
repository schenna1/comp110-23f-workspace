"""Exploring desgins."""
from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.color(173, 61, 216)
leo.speed(50)
leo.begin_fill()
leo.penup()
leo.goto(-100, -100)
leo.pendown()

bob: Turtle = Turtle()
bob.color(0, 0, 0)
bob.speed(100)
bob.penup()
bob.goto(-100, -100)
bob.pendown()

count = 0
while count < 3:
    leo.forward(300)
    leo.left(120)
    count += 1
leo.end_fill()
done()

side_length: float = 300
while count < 3:
    bob.forward(side_length)
    bob.left(120)
    count += 1
done()

while count < 30:
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(122)
    count += 1
done()