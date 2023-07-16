from turtle import Turtle , Screen
from time import sleep

# Starting_positions=[(0,0),(-21,0),(-42,0)]
Move_distance=20
Snake_speed=9   #in range 1-9
up=90
down=270
left=180
right=0

class Snake:
    def __init__(self,position,snake_color) -> None:
        self.snake_clr=snake_color
        self.bodyseg=[]
        self.bodyseg_start=[position,(position[0]-21,position[1]),(position[0]-41,position[1])]
        self.body()
        self.head=self.bodyseg[0]
        
    def body(self):
        
        for i in range(3):
            self.seg=Turtle(shape="square")
            self.seg.penup()
            self.seg.color(self.snake_clr)
            self.seg.goto(self.bodyseg_start[i])
            self.bodyseg.append(self.seg)
            
    def add_seg(self):
        self.seg=Turtle(shape="square")
        self.seg.hideturtle()
        self.seg.penup()
        self.seg.color(self.snake_clr)
        self.seg.goto(self.bodyseg[-1].position())
        self.bodyseg.append(self.seg)
        self.seg.showturtle()

    def move(self,S):
        for s in range(len(self.bodyseg)-1,0,-1):
            self.bodyseg[s].penup()
            x=self.bodyseg[s-1].xcor()
            y=self.bodyseg[s-1].ycor()
            self.bodyseg[s].goto(x,y)
        self.directions(S)
        self.head.fd(Move_distance)

    def menu_snake_move(self,x,y,Screen):
            self.xrange=x
            self.yrange=y
        
        
            for _ in range(int(self.xrange/20)):
                Screen.update()
                sleep(1-Snake_speed/10)
                for s in range(len(self.bodyseg)-1,0,-1):
                    self.bodyseg[s].penup()
                    x=self.bodyseg[s-1].xcor()
                    y=self.bodyseg[s-1].ycor()
                    self.bodyseg[s].goto(x,y)
                self.head.fd(Move_distance)
            self.head.right(90)


            for _ in range(int(self.yrange/20)):
                Screen.update()
                sleep(1-Snake_speed/10)
                for s in range(len(self.bodyseg)-1,0,-1):
                    self.bodyseg[s].penup()
                    x=self.bodyseg[s-1].xcor()
                    y=self.bodyseg[s-1].ycor()
                    self.bodyseg[s].goto(x,y)
                self.head.fd(Move_distance)
            
            self.head.right(90)

    def disappear1(self):
        for i in self.bodyseg:
            i.ht()


    def directions(self,S):
        S.listen()
        S.onkeypress(self.up,"Up")
        S.onkeypress(self.down,"Down")
        S.onkeypress(self.left,"Left")
        S.onkeypress(self.right,"Right")
        
    
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
        
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    


            