import turtle 
import random
# import colorgram
# tim1=turtle.Turtle()
tim=turtle.Turtle()
screen1=turtle.Screen()

# tim.shape("turtle")
# tim.color("red","yellow")
# tim.penup()
# tim.sety(300)
# tim.setx(-50)

# tim.pendown()

#for drawing square of lines
# tim.begin_fill()
# for i in range(4):
    
#     tim.fd(300)
#     tim.right(90)
# tim.end_fill()

#for drawing dashed lines
# for i in range(20):
#     tim.pendown()
#     tim.begin_fill()
#     for i in range(4):
#         tim.fd(10)
#         tim.right(90)
#     tim.end_fill()
#     tim.penup()
#     tim.fd(20)

#for drawing random shapes

shape_angles=[60,90,108,120,128.57,135,140,144]
shape_angles=shape_angles[::-1]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
sides=10
for i in range(8):
    tim.color(colours[i])
    tim.begin_fill()
    for j in range(sides):
        
        tim.fd(100)
        tim.right(180-float(shape_angles[i]))
    tim.end_fill()    
    sides-=1

# for random walk
screen1.colormode(255)
def random_clr():
    r=random.randint(0,225)
    g=random.randint(0,225)
    b=random.randint(0,225)
    return (r,g,b)
# screen.screensize(1000,1000)
# def random_dir(dir):
    

#     tim.color(random_clr())
#     if dir==1:
#         # tim.setheading(90)
#         tim.fd(15)
#     elif dir==2:
#         # tim.setheading(90)
#         tim.bk(15)
#     elif dir==3:
#         # tim.setheading(90)
#         tim.left(90)
#         tim.fd(15)
#     else:
#         # tim.setheading(90)
#         tim.right(90)
#         tim.fd(15)

# tim.pensize(7)
# tim.speed(0)
# tim.shape("circle")
# for _ in range(300):
    
#     random_dir(random.randint(1,5))



#for spirograph----------------------

# tim.pensize(5)
# tim1.pensize(3)
# tim.speed(0)
# tim1.speed(0)
# angle=90

# for i in range(int(360/5)):
#     tim.color((0,0,0))
#     tim.setheading(angle)
#     tim.circle(120)
#     for i in range(2):
#         tim1.color((0,0,0))
#         tim1.setheading(angle)
#         tim1.circle(200,90)
#         tim1.setheading(180+angle)
#         tim1.circle(200,90)
#     angle+=5


#for the painting------------------------------
# screen1.setup(1.0,1.0)
# screen1.setup(600,600)
# screen1.screensize(600,600)
# tim.color(random_clr())
# tim.speed(0)
# tim.pu()
# tim.setx(-250)
# tim.sety(-250)
# tim.pd()
# colors=colorgram.extract("Desktop-Wallpaper-Blackpink.jpg",20)
colors_lis=[(252, 199, 229), (241, 117, 178), (251, 153, 203), (242, 65, 139), (214, 226, 251), (63, 24, 45), (249, 215, 207), (141, 64, 113), (228, 143, 95), (124, 160, 210), (113, 33, 82), (165, 80, 45), (52, 100, 140), (25, 40, 57), (65, 29, 25), (180, 174, 236), (111, 109, 180), (196, 101, 73), (236, 171, 160), (53, 42, 129)]
#
# for clr in colors:
#     r=clr.rgb.r
#     g = clr.rgb.g
#     b = clr.rgb.b
#     new_color=(r,g,b)
#     colors_lis.append(new_color)
# print(colors_lis)
# for i in range(1,14):
#     for j in range(16):
#         tim.color(random.choice(colors_lis))
#         tim.begin_fill()
#         tim.dot(15)
#         tim.end_fill()
#         tim.pu()
#         tim.fd(30)
#         tim.pd()
#     tim.pu()
#     tim.setx(-250)
#     tim.sety(-250+i*40)
#     tim.pd()

# tim.setheading(70)
# tim.fd(150)
# tim.right(140)
# tim.fd(150)
# tim.right(180)
# tim.fd(75)
# tim.left(70)
# tim.fd(50)
# print(colors)
# tim.pu()
# tim.setx(-200)




screen1.mainloop()