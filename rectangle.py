import turtle
turtle.pencolor("black")

def draw_pixel(height,width,color):
    
    turtle.fillcolor(color)
    
    for i in range (4):
        turtle.pendown()
        turtle.begin_fill()
        turtle.right(90)
        turtle.forward(height) 
        turtle.right(90)
        turtle.forward(width)
        turtle.end_fill()
    turtle.penup()
    

def new_pixel(width):
    turtle.forward(width)
    

def draw_row(row,height,width,color):
    for a in range(row):
        draw_pixel(height,width,color)
        new_pixel(width)

def new_row(ycoor):
    turtle.goto(-150 ,ycoor)

def rectangle(row,column,height,width,color):
    ycoor = 150
    for b in range (column):
        new_row(ycoor)
        draw_row(row,height,width,color)
        ycoor = ycoor - height
        column = column + 1 

def main(rows,column,height,width,color="orange"):
    turtle.penup()
    turtle.speed(0)
    turtle.goto(-150,150)
    rectangle(rows,column,height,width,color)
    turtle.done()

main(20,5,30,15)
