import random
import turtle
from random import choice
from turtle import Turtle, Screen
turtle.colormode(255)

tim = Turtle()
tim.color("DarkCyan")
colors = ["red","orange","yellow","green","blue","indigo","purple"]
moves = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    a = (r, g, b)
    return a


def tim_rotate():
    tim.left(90)
    tim.left(90)

def start_pos():
    for i in range(1):
        tim.penup()
        tim.speed("fastest")
        tim.right(90)
        tim.forward(225)
        tim.right(90)
        tim.forward(225)
        tim_rotate()


def actual_draw():
    for i in range(10):
        tim.dot(20, random_color())
        tim.forward(50)

def restart_pos():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim_rotate()


tim.hideturtle()
start_pos()
for i in range(10):
    actual_draw()
    restart_pos()


screen = Screen()
screen.exitonclick()