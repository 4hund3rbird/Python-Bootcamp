from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json
window=Tk()
COMMAN_USER_NAME="kshirsagaraniket10@gmail.com"
charlist=list(range(33,48))
charlist+=list(range(58,65))
charlist+=list(range(91,97))
charlist+=list(range(123,127))
alpha=list(string.ascii_letters)
password_length=10
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
   
    
    def randomlist(n):
        password=alpha[random.randint(0,len(alpha)-1)]
        
        for i in range(0,n):
            b=random.randint(0,3)
            if b==0:
                try:
                    password+=alpha[random.randint(0,len(alpha))]
                except IndexError:
                    password+=alpha[random.randint(0,len(alpha)-1)]
            elif b==1:
                password+=chr(charlist[random.randint(0,len(charlist)-1)])
            else :
                password+=str(random.randint(0,10))
        return password

    new_password=randomlist(password_length)
    pyperclip.copy(new_password)
    password.insert(0,new_password)           

#-----------------------------Search Password--------------------------------
def search():
    try:
        with open("data.json","r") as datafile:
            old_data=json.load(datafile)
            old_website=old_data[website.get()]
            old_password=old_website["password"]
            old_user=old_website["username"]
            pyperclip.copy(old_password)
            messagebox.showinfo(title="My Password Manager",message=f"Your saved username and password is \nuser: {old_user} \npassword: {old_password}")
        pass
    except:
        messagebox.showerror(title="My Password Manager",message="There are none passwords saved!")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    my_data={website.get():{"username":user.get(),"password":password.get()}}
    if website.get()=="" or password.get()=="" or user.get()=="":
        messagebox.showwarning(title="My password manager",message="Don't leave any fields empty!")
    else: 
        is_ok=messagebox.askokcancel(title="My password manager",message=f"Website: {website.get()}\nEmail/Username: {user.get()}\nPassword: {password.get()}\nDo you want to save it?")
        if is_ok :
            try:
                with open("data.json","r") as file:
                    new_data=json.load(file)
                    new_data.update(my_data)
                    print(new_data)
            except:
                 with open("data.json","w") as file:
                    json.dump(my_data,file,indent=4)
                    website.delete(0,END)
                    password.delete(0,END)
            else:
                with open("data.json","w") as file:
                    json.dump(new_data,file,indent=4)
                    website.delete(0,END)
                    password.delete(0,END)

    pass

# ---------------------------- UI SETUP ------------------------------- #
window.title("My Password Manager")

myimage=PhotoImage(file="logo.png")

canvas=Canvas(width=200,height=200)
canvas.create_image(100,100,image=myimage)
window.config(padx=20,pady=20)

canvas.grid(row=0,column=0,columnspan=3)

#Labels------------------------------------------------
label1=Label(text="Website:")
label1.grid(row=1,column=0)
label2=Label(text="Email/Username:")
label2.grid(row=2,column=0)

label3=Label(text="Password:")
label3.grid(row=3,column=0)


#buttons-----------------------------------------------
button1=Button(window,text="Generate Password",command=generate_password,width=14)
button1.grid(row=3,column=2)
button2=Button(window,text="Add",width=33,command=add_pass)
button2.grid(row=4,column=1,columnspan=2)
button3=Button(window,text="search",width=14,command=search)
button3.grid(row=1,column=2)
#Entrys================================================
website=Entry(window,width=21)
website.focus()
website.grid(row=1,column=1)
user=Entry(window,width=40)
user.insert(0,COMMAN_USER_NAME)
user.grid(row=2,column=1,columnspan=2)
password=Entry(window,width=21)
password.grid(row=3,column=1)
window.mainloop()