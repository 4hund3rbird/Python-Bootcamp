from turtle import Turtle , Screen
from winsound import Beep
from snake import Snake
from food import Fruit
from scoreboard import Scorecard
from time import sleep
from menu import Menu
from random import randint
from zeptorrr import Zeptorrr

Snake_position=randint(-250,250)
Snake_speed=9   #in range 1-9
screen_height=600
screen_width=600
cx=300
cy=300

class game():
    def __init__(self) -> None:
        self.screen=Screen()
        self.screen.setup(screen_width,screen_height)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game in python")
        self.score=0
        self.highscore=0
        self.highscore_file()
        self.screen.tracer(0)
        self.menu_screen()
        self.screen.exitonclick()
    
    def highscore_file(self):
        with open("highscore.txt") as file:
            highscore_list=file.read().split("\n")
            self.highscore=int(highscore_list[-1])
    
    def single_player(self):
        self.screen.update()
        self.grid()
        self.game_is_on=True
        self.character()
        self.movement()
    
    def vs_zeptorrr(self):
        self.screen.update()
        self.grid()
        self.game_is_on=True
        self.vs_zeptorrr()
        self.movement()

    def menu_screen(self):
        self.menu=Menu(self.screen)
        while True:
            self.menu.snake_animation()
            if self.menu.game=="single_player":
                self.menu.disappear()
                self.single_player()
                break
            elif self.menu.game=="vs zeptorrr!":
                self.menu.disappear()
                self.vs_zeptorrr()
                break
    
    
    def grid(self):
        self.gridpen=Turtle()
        self.gridpen.color("grey")
        self.gridpen.pensize(0.5)
        self.gridpen.ht()
        
        
        j=0
        for i in range(30):
            self.gridpen.pu()
            self.gridpen.goto(cx,cy-j)
            self.gridpen.pd()
            self.gridpen.goto(-cx,cy-j)
            j+=19.8

        j=0
        for i in range(30):
            self.gridpen.pu()
            self.gridpen.goto(-cx+j,cy)
            self.gridpen.pd()
            self.gridpen.goto(-cx+j,-cy)
            j+=19.8
        self.screen.update()

    def character(self):
        self.character1=Snake((Snake_position,Snake_position),"green")
        self.food=Fruit()
        self.scorecard=Scorecard(self.score,self.highscore)

    def zeptorrr(self):
        self.character2=Zeptorrr((Snake_position,Snake_position),"red")
        self.character1=Snake((Snake_position,Snake_position),"green")
        self.food=Fruit()
        self.scorecard=Scorecard(self.score)


    def snake_collision(self):
        for seg in range(1,len(self.character1.bodyseg)):
            
            if self.character1.head.distance(self.character1.bodyseg[seg]) <10:
                self.game_is_on=False
                self.scorecard.game_over()

    def movement(self):
        while self.game_is_on:
            self.screen.update()
            sleep(1-Snake_speed/10)
            self.character1.move(self.screen)
            
            if self.character1.head.distance(self.food.obj)<=15:
                Beep(500,40)
                self.food.random_pos()
                self.character1.add_seg()
                self.score+=1
                if self.score>self.highscore:
                    self.highscore=self.score
                self.scorecard.clear()
                self.scorecard=Scorecard(self.score,self.highscore)
                print(self.highscore)
        
            
            if self.character1.head.xcor()>=cx or self.character1.head.ycor()>=cy or self.character1.head.xcor()<=-cx or self.character1.head.ycor()<=-cy:
                self.game_is_on=False
                Beep(600,600)
                self.scorecard.clear()
                self.scorecard.game_over()
                

            self.snake_collision()
        print(self.highscore)
        with open("highscore.txt","a") as file:
            file.write(f"\n{self.highscore}")
            
game1=game()