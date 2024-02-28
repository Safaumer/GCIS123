import turtle
def draw():
    turtle.speed(5)
    turtle.up()
    turtle.goto(-50,-50)
    turtle.down()
    turtle.goto(0,50)
    turtle.goto(50,-50)
    turtle.goto(-50,25)
    turtle.forward(100)
    turtle.goto(-50,-50)
    turtle.done()

def main():
    draw()
    
main()