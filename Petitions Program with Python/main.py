
from os import system
#------------------------------------Global variables-------------------------------------------------------------------------
#---------------------------------------function to write which user has how many petitions-------------------------------------------
def countpetitions(count,username):
    with open("count_petitions.txt","w") as count_user:
        count_user.write("\n"+username+"\n"+str(count))
        

# -----------------------------------------function to write petition through login-----------------------------------------------------
def logindec1(username):
    with open("count_petitions.txt","r") as count_user:
        countuser=count_user.read().strip().split("\n")
    a=countuser.index(username)
    count=int(countuser[int(a)+1])
    print("You can write your petition now")
    while True:
        
        user=username
        user+=str(count)+".txt"
        count+=1
        
        petition_title=input("Write title of the petition ...\n")
        petition=input("Start writing from here....  \n")
        with open(user,"w") as file:
            file.write(petition_title)
                
        with open(user,"a") as file:
            file.write("\n"+petition)
                    
        with open("users.txt","a") as file:
            file.write("\n"+user)
                
        with open(user[0:len(user)-4]+".sign.txt","w") as file:
            file.write(user[0:len(user)-4]) 
                
        dec3=input("your petition is stored\n\nPress 0 to write another one\n\nPress else any key to exit\n")
        if dec3=="0":
            continue
        else:
            break
    countpetitions(count,username)
#--------------------------------------Your activity function--------------------------------------------------------------------------

def youractivity(username):
    while True:
        act_dec=input("0 to petitions you have written\n1 to people signed to your petitions \n2 to sign a petition\n3 to make a petition\nelse any key to exit\n")
        if act_dec=="0":
            with open(username+".txt","r") as file:
                print(file.read())
            print("\n")    
        elif act_dec=="1":
            with open(username+".sign.txt","r") as file:
                a=file.read().strip().split("\n")
                print(len(a)," people signed to your petition")        
        elif act_dec=="2":
            dec2()
        elif act_dec=="3":
            logindec1(username)
        else:
            break
             
        
#-----------------------------------Function to login-----------------------------------------------------------------------------------
def login():
    
    username=input("Enter username here.. - ")
    fullname=username+".txt"
    with open("users.txt","r") as file:
        a=file.read().strip().split("\n")
                
    if fullname in a:
        youractivity(username)
    else:
        while True:
            print("You don't have any registered account\nMake one by writing a petition")
            dec100=input("0 to sign a petition\n1 to make a petition\nelse any key to exit\n")
            if dec100=="1":
                dec1()
            elif dec100=="0":
                dec2()
            else:
                break
        
                 
                
                
                    
    
    
    

#-----------------------------------Function to write petitions-------------------------------------------------------
def dec1():
    print("You can write your petition now")
    while True:
        user=input("enter your email address here \n")
        user+=".txt"
        with open("users.txt","r") as file:
            a=file.read().strip().split("\n")
        if user in a :
            print("You already have an account")
            youractivity()
            
                
        else:
            petition_title=input("Write title of the petition ...\n")
            petition=input("Start writing from here....  \n")
            with open(user,"w") as file:
                file.write(petition_title)
                
            with open(user,"a") as file:
                file.write("\n"+petition)
                    
            with open("users.txt","a") as file:
                file.write("\n"+user)
                
            with open(user[0:len(user)-4]+".sign.txt","w") as file:
                file.write(user[0:len(user)-4]) 
                
            dec3=input("your petition is stored\n\nPress 0 to write another one\n\nPress else any key to exit\n")
            if dec3=="0":
                continue
            else:
                break



#-----------------------------------Function to show all the stored petitions----------------------------------------



def dec2():
    while True:
        with open("users.txt","r") as file:
            userdata=file.read()
            petitions=userdata.strip().split("\n")
            print(petitions)
            
            
        c=0
        for i in petitions:
            with open(i,"r") as file:
                print(file.read()+"\n")
            print("Author of this petition is "+i[0:len(i)-4]+"\n")
            
            with open(i[0:len(i)-4]+".sign.txt","r") as file:
                peoples=file.read()
                peoples_signed=peoples.split("\n")
            print("----------------------------------------Number of peoples signed this petition == ",len(peoples_signed),"\n")    
            print("To sign this petiton press ",c,"\n")
            c+=1
        petition_no=int(input("------------------------------------- "))
        signed_petition=petitions[petition_no]
        signs(signed_petition)   
        dec4=input("Thanks for your response\n\nPress 0 to sign another petition\n\nPress else any key to exit\n") 
        if dec4=="0":
            continue
        else:
            break


#-------------------------------------------Function to sign petitions--------------------------------------------------
def signs(signed_petition):
    sign=input("Write your gmail here to sign the petition\n")
    with open(signed_petition[0:len(signed_petition)-4]+".sign.txt","r") as usersign:
        already_signed=usersign.read().strip().split()
        if sign in already_signed :
            print("You have signed this petition before")
        else:
            with open(signed_petition[0:len(signed_petition)-4]+".sign.txt","a") as usersign:
                usersign.write(sign+"\n")
    
        



#---------------------------------------------main fun------------------------------------------------------------------

print(""" 
      
      
            ██████╗░███████╗████████╗██╗████████╗██╗░█████╗░███╗░░██╗░██████╗    
            ██╔══██╗██╔════╝╚══██╔══╝██║╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝    
            ██████╔╝█████╗░░░░░██║░░░██║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░    
            ██╔═══╝░██╔══╝░░░░░██║░░░██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗    
            ██║░░░░░███████╗░░░██║░░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝    
            ╚═╝░░░░░╚══════╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░    

            ░█████╗░██████╗░███████╗        
            ██╔══██╗██╔══██╗██╔════╝        
            ███████║██████╔╝█████╗░░        
            ██╔══██║██╔══██╗██╔══╝░░        
            ██║░░██║██║░░██║███████╗        
            ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝        

            ██████╗░███████╗░█████╗░██╗░░░░░
            ██╔══██╗██╔════╝██╔══██╗██║░░░░░
            ██████╔╝█████╗░░███████║██║░░░░░
            ██╔══██╗██╔══╝░░██╔══██║██║░░░░░
            ██║░░██║███████╗██║░░██║███████╗
            ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝ 
            
            \n""")
sign=100
while True:
    system("cls")
    dec=input("0 to sign a petition\n1 to make a petition\n2 to login\nelse any key to exit\n")
    if dec=="1":
        dec1()
    elif dec=="0":
        dec2()
    elif dec=="2":
        login()    
        
          
    else:
        print("Thanks for your interest\n\n")
        print(""" 
                    ████████████████████████████████████████
                    ████████████████████████████████████████
                    ██████▀░░░░░░░░▀████████▀▀░░░░░░░▀██████
                    ████▀░░░░░░░░░░░░▀████▀░░░░░░░░░░░░▀████
                    ██▀░░░░░░░░░░░░░░░░▀▀░░░░░░░░░░░░░░░░▀██
                    ██░░░░░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░██
                    ██░░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░██
                    ██░░░░░░░░░░░░░░░░░▄▀░█░░░░░░░░░░░░░░░██
                    ██░░░░░░░░░░████▄▄▄▀░░▀▀▀▀▄░░░░░░░░░░░██
                    ██▄░░░░░░░░░████░░░░░░░░░░█░░░░░░░░░░▄██
                    ████▄░░░░░░░████░░░░░░░░░░█░░░░░░░░▄████
                    ██████▄░░░░░████▄▄▄░░░░░░░█░░░░░░▄██████
                    ████████▄░░░▀▀▀▀░░░▀▀▀▀▀▀▀░░░░░▄████████
                    ██████████▄░░░░░░░░░░░░░░░░░░▄██████████
                    ████████████▄░░░░░░░░░░░░░░▄████████████
                    ██████████████▄░░░░░░░░░░▄██████████████
                    ████████████████▄░░░░░░▄████████████████
                    ██████████████████▄▄▄▄██████████████████
                    ████████████████████████████████████████
                    ████████████████████████████████████████

                                                   ( ͡• ͜ʖ ͡•)     -------------YOUR SIGN CAN MAKE A CHANGE 
                  """)
        break     
        