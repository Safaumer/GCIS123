import turtle

def setpos(turta,x,y):
    turtle.up()
    turta=turtle.Turtle(x,y)

turtle.goto(50,50)
setpos(turta.goto,0,0)
turtle.goto(-50,-50)
turtle.done()
