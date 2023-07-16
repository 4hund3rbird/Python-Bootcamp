import turtle
from time import sleep
import pandas
tim=turtle.Turtle()
tim.ht()
tim.pu()
screen=turtle.Screen()
image="A:\PYTHON\Python Bootcamp\projects\CSV and pandas\India state game\india map blank.gif"
screen.addshape(image)
screen.setup(800,800)
turtle.shape(image)
data=pandas.read_csv("A:\PYTHON\Python Bootcamp\projects\CSV and pandas\India state game\india_states.csv")
state_name=data["states"]
state_x=data["x"]
state_y=data["y"]
state_name=state_name.tolist()
state_x=state_x.tolist()
state_y=state_y.tolist()
    
for i in range(len(state_name)):
    tim.goto(state_x[i],state_y[i])
    tim.write(state_name[i])
    
    


    

screen.mainloop()