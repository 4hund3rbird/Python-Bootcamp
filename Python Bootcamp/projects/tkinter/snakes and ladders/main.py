from turtle import RawTurtle, ScrolledCanvas,TurtleScreen, circle
from tkinter import *

window=Tk()
window.config(width=400,height=400)
boardcanvas=ScrolledCanvas(window)
boardimage=PhotoImage(file="board2.png")
boardcanvas.create_image(0,0,image=boardimage)
boardcanvas.config(height=800,width=1000)
boardcanvas.pack()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

window.bind('<Motion>', motion)



window.mainloop()