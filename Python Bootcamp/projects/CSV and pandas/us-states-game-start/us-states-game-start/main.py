import turtle
import pandas

class Data:
    def __init__(self) -> None:
        self.data=pandas.read_csv("50_states.csv")
        self.states=self.data["state"].tolist()
        self.guess=False

    def find_states(self,state_name):
        state_name=state_name.title()
        if state_name in self.states:
            self.states.remove(state_name)
            print(self.states)
            self.dataseries=self.data[self.data.state == state_name]
            self.x=int(self.dataseries.x)
            self.y=int(self.dataseries.y)
            self.pen=pen(state_name,self.x,self.y)
            self.guess=True
        else:
            pass

    def exit_data(self):
        missing_states_dictionary={
            "states":self.states
        }
        missing_states=pandas.DataFrame(missing_states_dictionary)
        missing_states.to_csv("missing states.csv")
    
class pen(turtle.Turtle):
    def __init__(self,state_name,x,y) -> None:
        super().__init__()
        self.ht()
        self.pu()
        self.goto(x,y)
        self.write(state_name,font=("arial",7,"normal"))      
    

class Setup:
    def __init__(self) -> None:
        self.run=0
        self.game_is_on=True
        self.screen=turtle.Screen()
        self.screen.setup(730,515)
        image="blank_states_img.gif"
        self.screen.addshape(image)
        turtle.shape(image)
        self.data=Data()
        self.main_loop()
        self.screen.exitonclick()

        

        
    def main_loop(self):
        while self.game_is_on:
            self.input_state()
            if self.run==50:
                self.game_is_on==False

    
    
    def input_state(self):
        self.state=self.screen.textinput(title=f"{self.run}/50 states",prompt="enter name of state here")
        self.data.find_states(self.state)

        if self.state=="exit":
            self.screen.bye()
            self.data.exit_data()
        
        if self.data.guess:
            self.run+=1


        

game1=Setup()