# Turtle is a native drawing library in Python and a way to have some fun or learn coding.
# It was a part of the original Logo Programming.

# Introduction to Turtle Graphics.
# Python's turtle graphics system displays a small cursor known as a turtle.

# <Turtle Function>
# forward() / bk() > move the turtle
# right() / left() > rotate the turtle
# circle() > draw a circle
# up() / down() > raise/lower the drawing pen
# goto() > move to x, y coordinate
# setheading() > set turtle orientation
# showturtle() / hideturtle() > set turtle visibility
# color() > set drawing color
#width() > set line width


import turtle
w = turtle.Screen()
turtle.showturtle()
turtle.shape('turtle')
turtle.shapesize(3)
turtle.color('green')

pen = turtle.Turtle()
turtle.forward(100)
pen.left(90)
pen.forward(75)
pen.circle(200)






