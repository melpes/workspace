import turtle as t
n=int(input()) #사용자의 입력을 받음
t.shape('arrow')

def shape1():
    global b
    b="3"
def shape2():
    global b
    b="4"
def shape3():
    global b
    b="5"
def shape4():
    global b
    b="6"
    
def shape(a,b): #a=색, b= 모양
    t.color(a)
    if b=="3":
        tri(50)
    if b=="4":
        square(50)
    if b=="5":
        penta(50)
    if b=='6':
        hexgon(50)
def drawit(x,y):
    global a
    global b
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    shape(a,b)
    t.end_fill()
    
def tri(length):
    for i in range(3):
        t.fd(length)
        t.left(120)
        
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def penta(length):
    for i in range(5):
        t.fd(length)
        t.left(72)

def hexagon(length):
    for i in range(6):
        t.fd(length)
        t.left(40)
        
s=turtle.Screen()
s.onkey(shape1,"3")
s.onkey(shape2,"4")
s.onkey(shape3,"5")
s.onkey(shape4,"6")
s.listen()
s.onscreenclick(drawit)