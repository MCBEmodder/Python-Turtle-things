import turtle
import random
bob = turtle.Turtle()
turtle.colormode(255)

# CFG:
# size to remove every time:
stret = 1
# size to start with:
startsize = 300
# pen colour:
bob.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))

turtle.Screen().tracer(False)

size = startsize
while size > 0:
    for i in range(32):
        for i2 in range(4):
            bob.forward(size)
            bob.right(90)
            bob.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        bob.right(11.25)
    size-= stret

turtle.Screen().exitonclick()
