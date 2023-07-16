list1 = []
list2 = []
mydict = {}

list1 = ["Animesh","ritik","aniket"]
list2 = [7058317006,1236547896,1236547899]

# print(list1)
# print(list2)

list3=zip(list1,list2)
for key in list3:
    mydict[key[0]]=key[1]
print(mydict)
# for key in range(0,len(list1)):
#     mydict[list1[key]]=list2[key]
# print("Dicitonary :\n",mydict)
