
# petitions=[]
# sign=0
 
# def dataassin(petition,user):
#     with open(user,"w") as file:
#         file.write(petition)
#         file.write("\n"+sign)
#     data(user)        

# def data(user):
#     with open("users.txt","a") as file:
#         file.write(user+"\n")
        
# def dottedline():
#     for i in range(0,150):
#         print('_',end="")
#     print("\n")

# def dec1():
#     print("You can write your petition now")
#     user=input("enter your email address here \n")
#     user+=".txt"
#     petition=input("Start writing from here....  \n")
#     dataassin(petition,user)
#     print("your petition is stored")

# def dec2():
#     with open("users.txt","r") as file:
#         userdata=file.read()
#         petitions=userdata.split("\n")
#     cont=0
#     for i in petitions:
#         with open(i,"r") as file:
#             print(file.read()+"\n")
#         print("Author of this petition is "+i[0:len(i)-4]+"\n")
       
        
#         print("To sign this petiton press ",cont,"\n")
#         cont+=1
#         dottedline()    
                    
# print("""This is a petition programme
# You can use this programme to sign or make petitions
# Do you like to make a petiton or sign an existing one\n""")


# dec1=int(input("0 to sign a petition\n1 to make a petition\n"))
# if dec1==1:
#     dec1()
   
# elif dec1==0:
#     dec2()    


