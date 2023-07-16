

#------------------------------------Global variables-------------------------------------------------------------------------





#-----------------------------------Function to write petitions-------------------------------------------------------
def dec1():
    print("You can write your petition now")
    while True:
        user=input("enter your email address here \n")
        user+=".txt"
        petition_title=input("Write title of the petition ...\n")
        petition=input("Start writing from here....  \n")
        with open(user,"w") as file:
            file.write(petition_title)
            file.write(petition)
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

print("""This is a petition programme
You can use this programme to sign or make petitions
Do you like to make a petiton or sign an existing one\n""")
sign=100
while True:
    dec=input("0 to sign a petition\n1 to make a petition\nelse to exit\n")
    if dec=="1":
        dec1()
    elif dec=="0":
        dec2()
        
          
    else:
        print("Thanks for your interest\n\n")
        print(""" 
                     @    @
                    @@@  @@@                
                   @@@@@@@@@@                             
                  @@@@@@@@@@@@
                  -------------YOUR SIGN CAN MAKE A CHANGE 
                  """)
        break     
        