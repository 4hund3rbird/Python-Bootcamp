from tkinter import *

root=Tk()
root.title("Hello World!!!")
def clickme():
    name="hello "+input1.get()
    mylabel=Label(root,text=name)
    mylabel.pack()
input1=Entry(root,borderwidth=10)
input1.pack()
input1.insert(0,"Enter your name here ")

label1=Label(root,text="Hello World!!!")
label1.pack()
button1=Button(root,text="click me",command=clickme,borderwidth=10)
button1.pack()



root.mainloop()