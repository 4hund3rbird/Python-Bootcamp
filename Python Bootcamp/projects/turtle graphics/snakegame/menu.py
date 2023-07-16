from pickle import TRUE
from turtle import Turtle,Screen
from snake import Snake
from time import sleep

starting_pos=(-100,200)

class Menu:
    def __init__(self,Screen) -> None:
        self.turtles=[]
        self.snake=Snake(starting_pos,"green")
        self.button()
        self.title()
        self.draw_region()
        self.screen=Screen
        self.game="none"
        self.screen.onclick(self.button_click)
        

    def title(self):
        p=Turtle()
        self.turtles.append(p)
        p.ht()
        p.pu()
        p.color("white")
        p.goto(0,-260)
        # p.write("Designed and developed by ANIKET",font=("comic sans",15,"normal"),align="center")
        p.goto(0,250)
        p.color("green")
        p.write("Snakes In Python :)",font=("cooper black",30,"normal"),align="center")
        p.color("white")
        p.goto(0,125)
        p.write("SINGLE PLAYER",font=("cooper black",12,"normal"),align="center")
        p.goto(0,25)
        p.write("VS ZEPTORRR !!!",font=("cooper black",12,"normal"),align="center")  
        p.goto(0,-75)
        p.write("EXIT",font=("cooper black",12,"normal"),align="center")
    
    def button(self):
        b=Turtle()
        self.turtles.append(b)
        b.ht()
        j=0
        for i in range(3):
            b.pu()
            b.goto(75,100-j)
            b.pd()
            b.pensize(4)
            b.setheading(90)
            b.color("blue")
            for k in range(2):
                b.begin_poly()
                b.begin_fill()
                b.fd(50)
                b.left(90)
                b.fd(150)
                b.left(90)
                b.end_poly()
                b.end_fill()
            j+=100

    def draw_region(self):
        s=Turtle()
        self.turtles.append(s)
        s.ht()
        s.pensize(4)
        s.color("green")
        k=0
        for _ in range(3):
            s.pu()
            s.goto(-75,150-k)
            s.pd()
            for _ in range(2):
                
                s.fd(150)
                s.right(90)
                s.fd(50)
                s.right(90)
            k+=100

    def button_click(self,x,y):
        print(x,y)
        if x in range(-75,76) and y in range(100,151):
            self.game="single_player"
        elif x in range(-75,76) and y in range(0,51):
            self.game="vs zeptorrr!"
        elif x in range(-75,76) and y in range(-100,-51):
            self.game="END"
            self.screen.exitonclick()
            self.screen.bye()
        print(self.game)
    
    def disappear(self):
        for i in self.turtles:
            i.clear()
        self.snake.disappear1()
        
    
    def snake_animation(self):
        
        self.snake.menu_snake_move(200,350,self.screen)

