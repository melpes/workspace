import random
import turtle

def draw_rect(x, y, color, d):
    turtle.penup()
    turtle.pencolor(color)

    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(d)
        turtle.left(90)

turtle.screensize(500, 500)

while True:
    a, b = random.randint(-250, 250), random.randint(-250, 250)
    color = f"#{0}{0}{0}{0}{0}{0}".format(random.randint(0, 16))
    d = random.randint(10, 40)
    draw_rect(a, b, color, d)