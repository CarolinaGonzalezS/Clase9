import turtle
n=int(input("ingrese el tamaño del cuadrado: "))
l=int(input("ingrese el numero de lados: "))
t=turtle.Pen()
def MiPoligono(tamaño, lados):
    for x in range(1,lados+1):
        t.forward(tamaño)
        a=360/lados
        t.left(a)

MiPoligono(n,l)
turtle.getscreen()._root.mainloop()