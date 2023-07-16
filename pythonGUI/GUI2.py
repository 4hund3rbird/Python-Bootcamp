from tkinter import *
root=Tk()
root.title("addition")
nos=Entry(root)
nos.grid(row=0,column=0,columnspan=2)
def add():
    a=nos.get()
    nos.delete(0,END)
    
    
    
        # do nothing    
button1=Button(root,text="+",padx=20,pady=20,command=add)
button2=Button(root,text="-",padx=20,pady=20)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)


root.mainloop()
