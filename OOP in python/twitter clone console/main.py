
from logo import logo
from data import tweets , user


class menu:
    def __init__(self) -> None:
        self.choice=int(input("Press 1 to create new account \nPress 2 to access your account\nPress 3 to read tweets\n")) 
        if self.choice==1:
            self.create_user()
        elif self.choice==2:
            self.accessaccount()
        elif self.choice==3:
            self.printtweets()

    def create_user(self):
        name=input("Enter your full name here ")
        username=input("Enter your username here ")
        user1=user()
        user1.create_account(name,username)

    def accessaccount(self):
        username=input("To access your account enter your username here > ")
        with open("users.txt","r") as data:
            file=data.read()
            file=file.split("\n")
            datafound=False
            for i in file:
                if i==username:
                    # with open(f"{username}.txt","r") as file1:
                    #     file2=file1.read()
                    #     print(file2)
                    #     datafound=True
                    #     file1.close()
                        break
            if datafound:
                pass
            else:
                print("sorry your data is not into our servers :(")
                    

    def printtweets(self):
        with open("tweets.txt","r") as tweets:
            tw=tweets.read()
            for i in tw:
                print(i)

if __name__ == "__main__":
    
    while True:
        print(logo)
        menu1=menu()
        continue1=input("Do you want to continue ??  y/n  \n")
        if continue1 == "y":
            pass
        elif continue1=="n":
            print("\nThank You :) ")
            break
            
    

