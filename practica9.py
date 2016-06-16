import time
from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)
#Genera el movimiento
for x in range(0,150):
	#5 es x y 0 en y
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.05)

tk.mainloop()