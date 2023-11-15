"""Turtle Project - Desgining a surreal pink home with 2 windows. Broke up the draw_window function into a function to draw the back and the window pane seperately. A flower next to the house uses additional functions from Turtle."""
__author__ = "730956810"

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.speed(50)


def main() -> None:
    """The Entrypoint of my scene."""
    draw_house(-100, -100, 200)
    draw_window(-70, 30, 50)
    draw_window(10, 30, 50)
    draw_door(-25, -100, 50, 70)
    draw_flower(-160, -100)


def draw_square(x: float, y: float, side: float) -> None:
    """Draws square of designated size."""
    i = 0
    leo.goto(x, y)
    while i < 4:
        leo.forward(side)
        leo.left(90)
        i += 1


def draw_house(x: float, y: float, house_side: float) -> None:
    """Draws square with a triangle on top for the house. Fills in with a cool desgin."""
    leo.color(173, 61, 216)
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    draw_square(x, y, house_side)
    leo.begin_fill()
    leo.left(90)
    leo.forward(house_side)
    leo.right(30)
    leo.forward(house_side)
    leo.right(120)
    leo.forward(house_side)
    leo.end_fill()


def draw_window_pane(x: float, y: float, side: float) -> None:
    """Draws the cubes for the window panes."""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.setheading(0.0)
    leo.color(0, 0, 0)
    draw_square(x, y, side)
    leo.forward(side / 2)
    leo.left(90)
    leo.forward(side)
    leo.left(90)
    leo.forward(side / 2)
    leo.left(90)
    leo.forward(side / 2)
    leo.left(90)
    leo.forward(side)


def draw_window(x: float, y: float, side: float) -> None:
    """Combines the square and window pane function to draw and fill the windows."""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.setheading(0.0)
    leo.color(255, 255, 255)
    leo.begin_fill()
    draw_square(x, y, side)
    leo.end_fill()
    draw_window_pane(x, y, side)


def draw_door(x: float, y: float, lenght: float, width: float) -> None:
    """Draws and fills a rectangle for the door."""
    leo.begin_fill()
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.setheading(0.0)
    i = 0
    while i < 2:
        leo.forward(width)
        leo.left(90)
        leo.forward(lenght)
        leo.left(90)
        i += 1
    leo.end_fill()


def draw_flower(x: float, y: float) -> None:
    """Draws a flower by the house for complexity."""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.color(143, 241, 141)
    leo.left(90)
    leo.forward(50)
    leo.color(249, 97, 226)
    leo.begin_fill()
    i = 0
    while i < 12:
        leo.circle(4)
        leo.forward(5)
        leo.right(30)
        i += 1
    leo.end_fill()


if __name__ == "__main__":
    main()
done()