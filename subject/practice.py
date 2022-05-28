import turtle

turtle.shape("turtle")

turtle.forward(100)
turtle.left(30)
while turtle.pos() != (0, 0):
    turtle.forward(100)
    turtle.left(30)
    print(turtle.pos() != (0, 0))

turtle.done()

print()