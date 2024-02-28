from turtle import Turtle, Screen
# this is to introduce turta


def draw_circle(turta, x, y, radius,color):
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.fillcolor(color)
    turta.begin_fill()
    turta.circle(radius)
    turta.end_fill()
    turta.up()
    print(turta.xcor(),turta.ycor())
    

def nose(turta,x,y,color,radius):
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.fillcolor(color)
    turta.begin_fill()
    turta.circle(radius)
    turta.end_fill()
    turta.up()
    print(turta.xcor(),turta.ycor())

def draw_centred_circle(turta,x,y,radius,color):
    new_y=y-radius
    draw_circle(turta,x,new_y,radius,color)
    turta.up()
    turta.goto(x,y)
    turta.down()


def draw_eye(turta,x,y,radius,layer3color,layer2color,layer1color):
    draw_centred_circle(turta,x,y,radius,layer3color)
    draw_centred_circle(turta,x,y,radius*0.7,layer2color)
    draw_centred_circle(turta,x,y,radius*0.3,layer1color)

def smile(turta):
    turta.pencolor("black")
    turta.up()
    turta.goto(50,-30)
    turta.left(90)
    turta.down()
    turta.fillcolor("white")
    turta.begin_fill()
    turta.circle(50,-180)
    turta.up()
    turta.goto(50,-30)
    turta.left(270)
    turta.down()
    turta.forward(100)
    turta.end_fill()


def main():

    wind =Screen()
    wind.bgcolor("black")
    t= Turtle()
    wind.tracer(False)
    draw_circle(t,0,-100,100,"yellow")
    nose(t,0,-1.278976924,"orange",5)
    draw_eye(t,-50,50,20,"white","black","blue")
    draw_eye(t,50,50,20,"white","black","blue")
    smile(t)
    wind.exitonclick()

main()


