from tkinter import *



class converter_interface:
    def __init__(self) -> None:
        self.value=0
        self.parameters=['mm','cm','m','km','miles']
        self.convert_parameters=[0,0]
        self.window=Tk()
        self.window.title("Value Converter")
        self.window.minsize(300,300)
        self.window.config(padx=30,pady=30)
        self.start_label()
        self.user_value()
        self.result_label()
        self.spinbox()
        self.button()
        self.window.mainloop()

    def user_value(self):
        self.input=Entry(width=7)
        self.input.insert(END,string="0")
        self.input.grid(row=1,column=0)
    
    def label(self,prom,r,c):
        label1=Label(text=prom,font=('arial',20,'bold'))
        label1.grid(row=r,column=c)

    def start_label(self):
        self.label("Converter Program",0,1)

    def result_label(self):
        self.label(str(self.value),1,3)
        self.label('=',1,1)
    
    def spinbox_used(self):
        self.convert_parameters[0]=self.spina.get()
        self.convert_parameters[1]=self.spinb.get()
        print(self.convert_parameters)
    
    def spinbox(self):
        self.spina=Spinbox(values=self.parameters,command=self.spinbox_used,width=5)
        self.spina.grid(row=2,column=0)

        self.spinb=Spinbox(values=self.parameters,command=self.spinbox_used,width=5)
        self.spinb.grid(row=2,column=2)

    def calculator(self):
        # 1 mile = 1.60934 km
        # 1 km = 1000 m
        # 1 m = 100 cm
        # 1 cm = 10 mm
        
        para_dict={
            "mile":1.60934,
            "km":1000,
            "m":100,
            "cm":10,
            "mm":1
        }
        pass

    def button(self):
        But1=Button(text="Convert",command=self.calculator)   
        But1.grid(row=2,column=1) 

converter=converter_interface()