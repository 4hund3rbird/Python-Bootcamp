#this is a python script for turtle crossing game in python

#following are the modules required for this script
from turtle import Turtle , Screen
from winsound import Beep
import random
import time


#this is our class turtle which we are going to use for the following Cars
class Car(Turtle):
    def __init__(self,l):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1,stretch_len=3)
        self.color(self.random_clr())
        self.randomm_road(l)
    
    def randomm_road(self,locations):
        location=random.choice(locations)
        self.pu()
        self.goto(location)

    def random_clr(self):       #this function returns random colors from the rgb color gamaut
        r=random.randint(0,225)
        g=random.randint(0,225)
        b=random.randint(0,225)
        return (r,g,b)

class score(Turtle):        #to track the score of player
    def __init__(self,l):
        super().__init__()
        self.ht()
        self.pu()
        self.goto(0,300-30)
        self.write(f"Level:{l}",font=("copper blace",20,"bold"),align="center")

    def game_over(self,l):
        self.ht()
        self.pu()
        self.goto(0,0)
        self.write(f"Game Over !! :( \n Your Score is {l}",font=("copper black",30,"bold"),align="center")

class Game:
    def __init__(self) -> None:
        #to setup mainscreen and some essential data members
        self.screen=Screen()
        self.screen.setup(600,600)
        self.level=1
        self.game_is_on=True
        self.cars=[]

        self.screen.colormode(255)
        self.screen.tracer(0)
        self.hero=Turtle()
        self.speed=5
        self.road_locations=[]
        self.road()

        self.score=score(self.level)
        self.hero.shape("turtle")
        self.hero.color("green")
        self.hero.pu()
        self.hero.setheading(90)
        self.hero.goto(0,-258)
        self.hero.shapesize(stretch_len=1,stretch_wid=1)
        self.screen.update()

        self.getting_cars()
        self.screen.exitonclick()


    def getting_cars(self):
        while self.game_is_on :
            self.screen.update()
            time.sleep(1-self.speed/10)
            self.player_controls() 
            self.level_complete()
            self.score.clear()
            self.score=score(self.level)
            self.car=Car(self.road_locations)
            self.cars.append(self.car)
            for j in self.cars:
                j.fd(30)
            self.collision_with_cars()

    def collision_with_cars(self):
        for i in self.cars:
            if i.distance(self.hero)<30 and self.hero.ycor() in range(int(i.ycor()-5),int(i.ycor()+5)):
                self.game_is_on=False
                self.score.game_over(self.level)
                
    def level_complete(self):
        if self.hero.ycor()>=270:
            self.hero.goto(0,-258)
            self.level+=1
            if self.speed/10<0.9:
                self.speed+=0.05
            
    def player_controls(self):
        self.screen.listen()
        def up():
            self.screen.update()
            Beep(450,70)
            self.hero.fd(30)

        self.screen.onkey(up,"Up")   
            

    def road(self):
        r=Turtle()
        r.ht()
        r.pu()

        i=30
        for _ in range(18):
            r.begin_poly()
            r.goto(-300,300-i)
            self.road_locations.append((300,300-i-15))
            r.pd()
            r.fd(600)
            r.pu()
            r.end_poly()
            i+=30
        self.road_locations.remove(self.road_locations[len(self.road_locations)-1])
game=Game()
