import turtle as t
import random
tim = t.Turtle()
# colors =['pale turquoise','steel blue','indigo','indigo','chocolate','red','blue','green','medium aquamarine','orange','deep pink']

directions = [0,90,180,270]
tim.pensize(10)
tim.speed(10)
t.colormode(255)
def random_rgb():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b= random.randint(0, 255)
    random_color = ( r, g, b)
    return random_color
for _ in range(300):
     tim.color(random_rgb())
     tim.forward(30)
     tim.setheading(random.choice(directions))