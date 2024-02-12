import turtle

def draw_pixel(size,color):
    turtle.pencolor("Black")
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    for i in range (4):
        turtle.forward(size) 
        turtle.right(90)
    turtle.penup()
    turtle.end_fill()


def new_pixel(size):
    turtle.forward(size)
    

def draw_row(row,size,color):
    for a in range(row):
        draw_pixel(size,color)
        new_pixel(size)

def new_row(ycoor):
    turtle.goto(-150 ,ycoor)

def square(row,column,size,color):
    ycoor = 150
    for b in range (column):
        new_row(ycoor)
        draw_row(row,size,color)
        ycoor = ycoor - 30
        

def main(rows,column,size,color="green"):
    turtle.penup()
    turtle.speed(0)
    turtle.goto(-150,150)
    square(rows,column,size,color)
    turtle.done()

main(5,5,30,"red")




