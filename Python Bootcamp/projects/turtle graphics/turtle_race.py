from turtle import Turtle, Screen
import random

class game:
    def __init__(self) -> None:
        self.colors=["grey","blue","green","yellow","black","orange","purple","pink"]
        self.turtles=["jerry","tom","pikachu","thanos","joker","truman","levi","nobita","optimus"]
        self.turtles_list=["grey","blue","green","yellow","black","orange","purple","pink"]
        self.screen=Screen()
        self.screen.title("Turtle race .exe")
        self.screen.setup(width=500,height=500)
        self.finishline=Turtle()
        self.finish_line()
        self.turtle_assign()
        self.turtles_position()
        self.choose()
        self.random_walk()
        self.print_winner()
        self.screen.exitonclick()
    
    def finish_line(self):
        self.finishline.color("red")
        self.finishline.speed(0)
        self.finishline.pensize(3)
        self.finishline.ht()
        self.finishline.penup()
        self.finishline.goto(230,210)
        self.finishline.pendown()
        self.finishline.goto(230,-230)
        self.finishline.ht()
        

    def turtle_assign(self):
        for i in range(0,8):
            self.turtles[i]=Turtle(shape="turtle")
            self.turtles[i].ht()
            self.turtles[i].color(self.colors[i])

    def turtles_position(self):
        gap=-220
        for i in range(0,8):
            self.turtles[i].penup()
            self.turtles[i].goto(-230,gap)
            self.turtles[i].pendown()
            self.turtles[i].st()
            gap+=60
        
    def random_walk(self):
        while 1:
            i=random.randint(0,7)
            if self.turtles[i].xcor() >= 230:
                self.winner=i
                break
            self.turtles[i].forward(random.randint(0,10))
    
    def choose(self):
        self.chosen_one=self.screen.textinput("Turtle Race",f"Type the name of your turtle from{self.turtles_list}")
    
    
    def print_winner(self):
        self.message=f"The winner of this race is {self.turtles_list[self.winner]}"
        
        if self.turtles_list[self.winner]==self.chosen_one:
            self.message+="\nCongratulations!!!! :)"
        else:
            self.message+="\nsorry you loose :("
        self.winner_screen()

    def winner_screen(self):
        self.pen=Turtle()
        self.style=('Arial', 20, 'italic')
        self.pen.write(self.message,font=self.style,align='center')

game1=game()