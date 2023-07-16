BACKGROUND_COLOR = "#B1DDC6"
from cgitb import text
from textwrap import fill
from tkinter import *
from turtle import right, xcor
import pandas
import random
import time

#----------------------------data frame-------------------------------
word_data=pandas.read_csv("data/french_words.csv")
global word_to_learn
word_to_learn=[]
data_list=word_data.to_dict(orient="records")
#----------------------------commands--------------------------------
def next_card():
    global current_card 
    global flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(data_list)
    french_word=current_card["French"]
    canvas1.itemconfig(back_side,image=front_image)
    canvas1.itemconfig(title,text="French",fill="black")
    canvas1.itemconfig(word,text=french_word,fill="black")
    flip_timer=window.after(3000,func=flip_card)

def unknow_card():
    word_to_learn.append(current_card)
    data_list.remove(current_card)
    words=pandas.DataFrame(word_to_learn)
    words.to_csv("data/words_to_learn.csv")
    

    next_card()

def flip_card():
    canvas1.itemconfig(back_side,image=back_image)
    canvas1.itemconfig(title,text="English",fill="white")

    english_word=current_card["English"]
    canvas1.itemconfig(word,text=english_word,fill="white")

if __name__=="__main__":
    #-----------------------------UI setup---------------------------------
    window=Tk()
    window.title("Flash cards")
    window.config(background=BACKGROUND_COLOR,padx=50,pady=50)
    front_image=PhotoImage(file="images/card_front.png")
    back_image=PhotoImage(file="images/card_back.png")
    canvas1=Canvas(window,background=BACKGROUND_COLOR,highlightthickness=0,width=800,height=530)
    back_side=canvas1.create_image(400,265,image=front_image)

    #--------------------------text creation-----------------------------------
    title=canvas1.create_text(400,120,text="Flash cards word gussing game",font=('Ariel',30,"italic"))
    word=canvas1.create_text(400,250,text="Let's Start!",font=('Ariel',60,"bold"))
    canvas1.grid(row=0,column=0,columnspan=2)


    #------------------------Button creation-----------------------------------
    cross=PhotoImage(file="images/wrong.png")
    right=PhotoImage(file="images/right.png")


    right_button=Button(image=right,highlightthickness=0,command=unknow_card)
    right_button.grid(row=1,column=0)
    cross_button=Button(image=cross,highlightthickness=0,command=next_card)
    cross_button.grid(row=1,column=1)
    flip_timer=window.after(3000,func=flip_card)

    next_card()
    window.mainloop()

