import turtle
import os
ventana=turtle.Screen()
ventana.bgcolor("blue")
n=1
l=180
t=turtle.Pen()
a=0
def Letra():
    t.reset()
    t.color(1,0,0)
    t.begin_fill()
    t.forward(100)
    t.right(180)   
    t.forward(100)
    t.right(90)
    t.forward(100) 
    t.right(90)
    t.forward(100) 
    t.right(270)
    t.forward(20)
    t.right(270)
    t.forward(120)
    t.right(270)
    t.forward(140)
    t.right(270)
    t.forward(120)
    t.right(270)
    t.forward(20)
    t.end_fill()


Letra()

turtle.getscreen()._root.mainloop()