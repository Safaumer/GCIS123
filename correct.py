import turtle as t


def Squares():
    t.fillcolor("white")
    while i==(5):
        t.begin_fill()
        i+=1
        while w==(4):
            t.forward(30)
            t.right(90)
            w+=1
        t.end_fill()
        t.forward(30)
    t.done()

t.penup()
t.goto(-100,0)
t.pendown()
Squares()