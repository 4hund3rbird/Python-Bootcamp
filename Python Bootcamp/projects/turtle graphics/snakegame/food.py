from turtle import Turtle
import random
range_positive=290
range_negative=-290
class Fruit:

    def __init__(self) -> None:
        self.obj=Turtle(shape="circle")
        self.obj.color("red")
        self.obj.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.random_pos()

    def random_pos(self):
        self.x=random.randint(range_negative,range_positive)
        self.y=random.randint(range_negative,range_positive)
        self.obj.pu()
        self.obj.goto(self.x,self.y)


        
