import turtle
n=int(input("ingrese el tamaño del cuadrado: "))
t=turtle.Pen()

def CreacionCuadrado(tamaño):
	for x in range(1,5):
		t.forward(tamaño)
		t.left(90)

CreacionCuadrado(n)
turtle.getscreen()._root.mainloop()