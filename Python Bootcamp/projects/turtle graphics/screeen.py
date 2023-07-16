from random import choice
from turtle import Turtle, Screen

class character:
    def __init__(self,color,size):
        self.color=color
        self.size=size
        self.obj = Turtle()
        self.screen=Screen()
        self.colors=[(252, 199, 229), (241, 117, 178), (251, 153, 203), (242, 65, 139), (214, 226, 251), (63, 24, 45), (249, 215, 207), (141, 64, 113), (228, 143, 95), (124, 160, 210), (113, 33, 82), (165, 80, 45), (52, 100, 140), (25, 40, 57), (65, 29, 25), (180, 174, 236), (111, 109, 180), (196, 101, 73), (236, 171, 160), (53, 42, 129)]
        self.screen.colormode(255)
        self.obj.pensize(10)
        
    def moveup(self):
        self.obj.color(choice(self.colors))
        # self.obj.setheading(90)
        self.obj.forward(50)

    def movedown(self):
        self.obj.color(choice(self.colors))

        # self.obj.setheading(90)
        self.obj.backward(50)
    
    def moveright(self):
        self.obj.color(choice(self.colors))

        # self.obj.setheading(90)
        self.obj.right(90)
        self.obj.forward(50)
    
    def moveleft(self):
        self.obj.color(choice(self.colors))
        # self.obj.setheading(90)
        self.obj.left(90)
        self.obj.forward(50)

   
    def print_screen(self):
        self.obj.shape("turtle")
        self.obj.shapesize(self.size)
        self.obj.color(self.color)
        self.screen.onkeypress(self.moveup,"Up")
        self.screen.onkey(self.movedown,"Down")
        self.screen.onkey(self.moveleft,"Left")
        self.screen.onkey(self.moveright,"Right")
        self.screen.listen()
        self.screen.mainloop()
        
       

turtle1=character("green",2)
turtle1.print_screen()


# import prettytable

# table=prettytable.PrettyTable()
# table.add_column("Pokemon",["pikachu","charizard","squittle","balbasorus"])
# table.add_column("Type",["electric","fire","water","plant"])
# print(table)





# timmy1=character("Red",2)
# timmy1.print_screen()
#
#
