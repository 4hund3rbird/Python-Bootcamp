# dict1={"a":8,"n":7,"i":67,"k":49,"e":96 ,"t":91 }
# name=input("Enter username here: ")
# password=8767499691
# rivers={
#         "india":"brahamaputra",
#         "egypt":"nile",
#         "america":"amazon"
#         }
# for country,river in rivers.items():
#     print(river+" flows through "+country)
poll_people={ 
              "andy":"c",
              "aniket":"c++",
              "rahul":"python",
              "max":"java"
              }
total_people=["aniket","sumit","ashish","vivek","max","aditya","rahul","andy"]
for people in total_people:
    if people in poll_people.keys():
        print("thanks for giving us your opinion "+people)
    else :
        print("We are inviting you "+people)     