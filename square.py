import turtle


def square(x):
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.home()

def main():
    square(100)
    square(80)
    square(60)


def color():
    qwert=input("colour enter ")
    turtle.fillcolor(qwert)
    turtle.begin_fill()
    main()
    turtle.end_fill()


x=0
if x in range(0,4):
    color()
    x+=1

