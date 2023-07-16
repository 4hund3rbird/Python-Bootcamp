class user:
    def __init__(self,name):
        self.username=name
        self.followers=0
        self.following=0
        self.followerslist=[]
        print(f"New user {self.username} is created ")

    def follow(self,user):
        self.following+=1
        user.followers+=1
        user.followerslist.append(self.username)
        print(f"{self.username} started following {user.username} .")

if __name__ ==  "__main__" :
    user1=user("Aniketksagar1232")
    user2=user("sakshi")
    user2.follow(user1)
    print(f"{user1.followers}\n{user1.following}\n{user1.followerslist}\n{user2.followers}\n{user2.following}\n{user2.followerslist}\n")



