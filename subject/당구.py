from turtle import *
from random import *

WIN_WIDTH, WIN_HEIGHT = 500, 300
HALF_WIN_WIDTH, HALF_WIN_HEIGHT = WIN_WIDTH / 2, WIN_HEIGHT / 2
screensize(WIN_WIDTH, WIN_HEIGHT)
setup(550, 350)

class Ball:
    dirx, diry = 2, 2

    def __init__(self, x, y, dirx, diry, turt : Turtle, color) -> None:
        self.x, self.y = x, y
        self.dirx, self.diry = dirx, diry
        self.turt = turt
        self.turt.shape("circle")
        self.turt.speed(10)
        self.turt.color(color)
    
    def move(self):
        self.x += self.dirx
        self.y += self.diry

        if self.x < -HALF_WIN_WIDTH or self.x > HALF_WIN_WIDTH:
            self.dirx *= -1
        if self.y < -HALF_WIN_HEIGHT or self.y > HALF_WIN_HEIGHT:
            self.diry *= -1

        self.turt.penup()
        self.turt.goto(self.x, self.y)

t = []
colors = ["#1f1e33", "#00ff00", "#0088ff", "#f2ac53"]
for _ in range(4):
    x, y, dirx, diry = randrange(-250, 251), randrange(-150, 151), randrange(-10, 11), randrange(-10, 11)
    t.append(Ball(x, y, dirx, diry, Turtle(), choice(colors)))

while True:
    for i in range(4):
       t[i].move()

done()