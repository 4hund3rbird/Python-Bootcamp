# a=5
# a=int(input())

# for i in range(1,a+1):
#     for j in range(0,i):
#         print('*',end=" ")
        
#     print()        
# for i in range(a,0,-1):
#     for j in range(0,i):
#         print('*',end=" ")
        
#     print()    
#list operations
l1=[10,20]
l1.append(30)  #adds at the last of list
print(l1)
l1.insert(1,1) #inserts value at given index
print(l1)
l1[1]=10
print(l1)
l1.pop(0)
print(l1)
l1.remove(10)
print(l1)
l2=[]
a=10
for i in range(0,a):
    l2.append(i)
print(l2)    
print(l2.index(5))    
print(l2.count(1))
print(l2.sort())
print(l2.reverse())
print(l2)