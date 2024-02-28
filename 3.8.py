import turtle

angle=60
angle1=90
side=100

def square(x):
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(angle)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.home()
    turtle.end_fill()

def square2(x):
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.left(angle)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.home()
    turtle.end_fill()

def square3(x):
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.left(angle)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.forward(x)
    turtle.right(angle1)
    turtle.home()
    turtle.end_fill()
def main(x):
    square(x)
    
    turtle.done()

asdf=int(input("ENter size num:"))
main(asdf)

