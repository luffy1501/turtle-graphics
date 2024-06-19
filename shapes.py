from turtle import Turtle,Screen
import random
t = Turtle()
screen = Screen()
colors =['pale turquoise','steel blue','indigo','indigo','chocolate','red','blue','green','medium aquamarine','orange','deep pink']
def draw_shape(no_of_sides):
    for _ in range (no_of_sides):
        angle = 360/no_of_sides
        t.forward(100)
        t.right(angle)


for sides in range(3, 11):
    t.color(random.choice(colors))
    draw_shape(sides)
screen.exitonclick()