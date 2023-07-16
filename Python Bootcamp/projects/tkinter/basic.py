import tkinter

#window
window=tkinter.Tk()  #this is used to create window like screen in turtle
window.minsize(width=400,height=400)  #this is the size of window
window.title("This is a tkinter program >>") #this is title for the window
window.config(padx=20,pady=20)
#label
label=tkinter.Label(text="Hello World",font=("copper black",20,"bold")) #this is lable like we used to write in turtle
label.grid(row=0,column=0)
# label.grid(column=0,row=1) # this is grid system used to place objects on the screen in a grid like placement
# label1.grid(column=0,row=2)

#input field
input=tkinter.Entry(width=15)  # entry is used to get text input in window
prompt=input.get() # this returns a string which is inputed
input.grid(row=2,column=3)  # we have to pack every widget on window as everything in tkinter is an widget


#button
def button_clicked():   # function of button when got clicked
    label.config(text=input.get())
    print(prompt)

button=tkinter.Button(text="click to display",command=button_clicked) # to create a buttton
button.grid(row=1,column=1)

button1=tkinter.Button(text="Oh Yeah!!")
button1.grid(row=0,column=2)
window.mainloop() # this is the main loop which is used to listen for the actions on the screen

# class interface(tkinter.Tk):
#     def __init__(self) -> None:
#         super().__init__()
#         self.title("gui")
#         self.minsize(width=400,height=300)
#         self.button()
    
#     def label2(self,prompt):
#         label1=tkinter.Label(text=prompt,font=('arial',30,'bold'))
#         label1.pack()
    
#     def button_clicked(self):
#         self.label2("button is clicked")

#     def button(self):
#         button1=tkinter.Button(text="click me",font=('arial',10,'bold'),command=self.button_clicked)
#         button1.pack()

# interface1=interface()

# interface1.mainloop()