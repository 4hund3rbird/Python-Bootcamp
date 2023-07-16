from datetime import datetime

class tweets:
    def __init__(self,username):
        self.username=username
        self.tweet=""
        self.time=datetime.now()
        
    
    def maketweet(self):
        self.tweet=input("Start writing your tweet from here >  ")
        with open("tweets.txt","a") as user:
            user.write(f"\n{self.username}\n{self.tweet}\n{self.time}")
            user.close()
    
class user:
    def __init__(self) -> None:
        self.username=""
        self.name=""
        self.followers=[]
        self.following=[]
        tweet=tweets(self.username)
        self.tweet=tweet
    
    def login(self):
        pass
      
    def create_account(self,name,username):
        self.username=username
        self.name=name
        self.userfile=username+".txt"
        with open(self.userfile,"w") as userdata:
            userdata.close()

        with open("users.txt","a") as user2:
            user2.write(f"\n{username}")
            user2.close()

    def follow(self,user):
        self.following.append(user.username)
        user.followers.append(self.username)
        with open(self.userfile,"a") as userdata:
            userdata.write(self.following)
            userdata.write(self.followers)
            userdata.close()

    def unfollow(self,user):
        self.following.remove(user.username)
        user.followers.remove(self.username)

    def tweetit(self):
        self.tweet.maketweet()
        



