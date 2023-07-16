from random import randint
a=0
print("this is a guessing game ")
print("You have only 5 guesses ")

Properguess=randint(0,100)

print(Properguess)
# while True:
#     guess=int(input("Enter guess here : " ))
#     a+=1
#     if guess>=Properguess+50 :
#         print("You are going tob far ")
#     elif guess<=Properguess-10 :
#         print("Go far  bit ")

#     # elif (guess>Properguess-3) or (guess<Properguess+3) :
#     #     print("It is here somewhere!")    
    
#     elif guess==Properguess:
#         print("You Won!!!!")
#         break
