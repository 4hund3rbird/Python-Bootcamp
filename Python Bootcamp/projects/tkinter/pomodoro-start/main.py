from tkinter import *
from tkinter import font
from time import sleep
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE="#198bdd"
NAVY="#154c79"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE_DIM='465 x 319'



class promodoro_app:
    def __init__(self) -> None:
# ---------------------------- UI SETUP ------------------------------- #
        self.time=[24,59,4,20]
        self.reps=0
        self.window=Tk()
        self.window.title("Promodoro Application")
        self.window.config(pady=60,padx=50,bg=BLUE)
        self.timer_button_click=0
        self.reset_button_click=False
        #timer label
        self.label1=Label(text="Timer",font=("copper black",30,"bold"),fg="white",bg=BLUE)
        self.label1.grid(row=0,column=1)

        #check mark label   
        self.label2=Label(text="✓",font=("arial",20,"bold"),fg=NAVY,bg=BLUE)
        self.label2.grid(row=2,column=1)

        self.canvas=Canvas(width=450,height=300,bg=BLUE,highlightthickness=0)
        self.image=PhotoImage(file="image.png")
        self.canvas.create_image(220,150,image=self.image)
        self.buttons()
        self.timex=self.canvas.create_text(175,140,text=f"{self.time[0]}:{self.time[1]}",fill="white",font=("arial",30,"bold"))
        self.canvas.grid(row=1,column=1)

        
        self.window.mainloop()
        
    def buttons(self):
        button1=Button(text="Start",fg="white",bg=NAVY,width=8,highlightthickness=0,command=self.start_button_click)
        button1.grid(row=2,column=0)

        button2=Button(text="Reset",fg='white',bg=NAVY,width=8,highlightthickness=0)
        button2.grid(row=2,column=2)
        
    def start_button_click(self):
        self.reset_button_click=False
        self.counter()
        
    
    def reset_button_click(self):
        self.reset_button_click=True
# ---------------------------- TIMER MECHANISM ------------------------------- # 
    def counter(self):
        if self.timer_button_click == 0:
            
            if True :
                self.reps+=1
                print(self.reps)
                if self.reps==8:
                    self.timer(self.time[3],self.time[1])
                elif self.reps%2 != 0:
                    self.timer(self.time[0],self.time[1])
                elif self.reps%2==0:
                    self.timer(self.time[2],self.time[1])
            self.timer_button_click +=1
        else:
            pass


    def timer(self,h,m):
        
        if m < 0:
            m=59
            h=h-1
        if h < 0 :
            self.counter()
        if h>=0 :
            self.time[0]=f"{h}"
            self.time[1]=f"{m}"
            if h < 10:
                self.time[0]="0"+self.time[0]
            if m < 10:
                self.time[1]="0"+self.time[1]

            self.canvas.itemconfig(self.timex,text=f"{self.time[0]}:{self.time[1]}")
            self.window.after(10,self.timer,h,m-1)
        
# ---------------------------- TIMER RESET ------------------------------- # 


        

        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
    
            



#----------------------------- CLASS CALL -----------------------------------#
app1=promodoro_app()