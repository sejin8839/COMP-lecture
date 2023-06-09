# Turtle is a native drawing library in Python and a way to have some fun or learn coding.
# It was a part of the original Logo Programming.

# Introduction to Turtle Graphics.
# Python's turtle graphics system displays a small cursor known as a turtle.

# Don't forget <turtle.exitonclick()>


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



#<Making a rectangle>
#import turtle
#turtle.forward(100)
#turtle.left(90)
#turtle.forward(100)
#turtle.left(90)
#turtle.forward(100)
#turtle.left(90)
#turtle.forward(100)
#turtle.exitonclick()


#<pendown/penup>
#import turtle
#turtle.forward(50)
#turtle.penup()
#turtle.forward(25)
#turtle.pendown()
#turtle.forward(50)
#turtle.penup()
#turtle.forward(25)
#turtle.pendown()
#turtle.forward(50)
#turtle.exitonclick()


#<Drawing a circles>
#import turtle
#turtle.shape('turtle')
#turtle.color('green')
#turtle.circle(100)


#<Drawing a dot>
#import turtle
#turtle.dot()
#turtle.forward(50)
#turtle.dot()
#turtle.forward(50)
#turtle.dot()
#turtle.forward(50)
#turtle.exitonclick()


#<Changing the Pen Size and Drawing Color>
#import turtle
#turtle.pensize(5)
#turtle.pencolor('red')
#turtle.circle(100)


#<Resetting the turtle>
#import turtle
#turtle.setup(480, 240)


#<Moving the Turtle to a Specific Location>
#import turtle
#turtle.goto(0,100)
#turtle.dot()
#turtle.goto(-100,0)
#turtle.dot()
#turtle.goto(0,0)


#<Speed>



#<hiding and Displaying>




#Displaying test
#import turtle
#turtle.write('Hello World')
#turtle.style('courier',20)


#Filling Shapes
#import turtle
#turtle.hideturtle()
#turtle.fillcolor('red')
#turtle.begin_fill()
#turtle.circle(100)
#turtle.end_fill()
#turtle.exitonclick()


#import turtle
#turtle.pensize(5)
#turtle.pencolor('yellow')
#turtle.Turtle()
#for i in range(5):
    #turtle.forward(50)
    #turtle.right(144)
#turtle.exitonclick()


# Turtle shape
# from turtle import *
# speed(10)
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


color = ["red","purple","blue","green","orange","yellow"]
colorIndex = 0

import turtle
window = turtle.Screen()
turtle.bgcolor("black")
Apple = turtle.Turtle()
Apple.speed(10)
Apple.shape("circle")
Apple.color('red')
Apple.penup()
Apple.goto(50,50)
Apple.pendown()
appleWidth = 3
dotSize = 2
for x in range(1, 200, 3):
    Apple.pencolor(color[colorIndex%6])
    Apple.forward(x)
    Apple.left(120)
    Apple.dot(dotSize,"black")
    Apple.right(60)
    Apple.dot(dotSize,"black")
    Apple.width(appleWidth)
    colorIndex += 1

    # It increases width AND dotSize in every loop
    appleWidth += 0.1
    dotSize += 2
turtle.exitonclick()

# import turtle
# window = turtle.Screen()
# turtle.bgcolor("black")
# colors = [
# "red","purple","blue","green","orange","yellow"]
# Apple = turtle.Turtle()
# Apple.speed(10)
# Apple.shape("circle")
# Apple.penup()
# Apple.goto(50,50)
# Apple.pendown()
# appleWidth = 3
# dotSize = 2
#
# for x in range(1,200,3):
#
#     # for y in range(360):
#     #     Apple.color(colors[y % 6])
#     Apple.forward(x)
#     Apple.left(120)
#     Apple.dot(dotSize,"black")
#     Apple.right(60)
#     Apple.dot(dotSize,"black")
#     Apple.width(appleWidth)
#
#     # It increases width AND dotSize in every loop
#     appleWidth += 0.1
#     dotSize += 2


turtle.exitonclick()



# import turtle library
# # import turtle
# colors = [
# "red","purple","blue","green","orange","yellow"]
# my_pen = turtle.Pen()
# turtle.bgcolor("black")
# for x in range(360):
#     my_pen.pencolor(colors[x % 6])
#     my_pen.width(x/100 + 1)
#     my_pen.forward(x)
#     my_pen.left(59)
# done()
#
# # turtle demo examples
# # Terminal 부분에 <python -m turtledemo> 입력하기




# import turtle
# window = turtle.Screen()
# spiral = turtle.Turtle()
# spiral.color('green')
# spiral.penup()
# spiral.goto(0,-100)
# spiral.pendown()
# spiral.width(1)
# for x in range(1,200,5):
#     spiral.forward(x)
#     spiral.left(90)
# turtle.exitonclick()


#turtle.showturtle()
#turtle.shape('turtle')
#turtle.shapesize(3)
#turtle.color('green')




