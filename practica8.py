from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()

my_image= PhotoImage(file="ball.gif")
#ubicacion de la imagen
canvas.create_image(10,10, ancho=NW, image=my_image)
canvas.create_image(20,20, ancho=NW, image=my_image)
canvas.create_image(30,30, ancho=NW, image=my_image)
canvas.create_image(40,40, ancho=NW, image=my_image)
canvas.create_image(50,50, ancho=NW, image=my_image)
canvas.create_image(60,60, ancho=NW, image=my_image)
canvas.create_image(70,70, ancho=NW, image=my_image)
canvas.create_image(80,80, ancho=NW, image=my_image)
canvas.create_image(90,90, ancho=NW, image=my_image)
canvas.create_image(100,100, ancho=NW, image=my_image)
canvas.create_image(110,110, ancho=NW, image=my_image)
canvas.create_image(120,120, ancho=NW, image=my_image)
canvas.create_image(130,130, ancho=NW, image=my_image)
canvas.create_image(140,140, ancho=NW, image=my_image)
canvas.create_image(150,150, ancho=NW, image=my_image)


tk.mainloop()