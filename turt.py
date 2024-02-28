import turtle

def turtlestate():
    print(turtle.isdown())
    print(turtle.heading())
    x=turtle.xcor()
    y=turtle.ycor()
    print(x,"x coordinate",y,"y coordinate")

def triangle():
    turtle.forward(100)
    turtle.goto(50,80)
    turtle.home()

def square():
    turtle.right(180)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

def circle():
    turtle.circle(25)


def main():
    turtlestate()
    triangle()
    turtlestate()
    square()
    turtlestate()
    circle()
    turtle.done()

main()