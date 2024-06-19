import turtle as t
import random
tim = t.Turtle()


tim.speed(1000)
t.colormode(255)
def random_rgb():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b= random.randint(0, 255)
    random_color = ( r, g, b)
    return random_color
for _ in range(1000):
    tim.color(random_rgb())
    tim.circle(100)
    tim.setheading(tim.heading() + 10)

screen = t.Screen()
screen.exitonclick()