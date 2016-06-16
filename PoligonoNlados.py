import turtle
n=int(input("ingrese el numero de lados: "))
t=turtle.Pen()

for x in range(1,n+1):
    t.forward(50)
    a=360/n
    t.right(a)

turtle.getscreen()._root.mainloop()