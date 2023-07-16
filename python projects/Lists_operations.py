a=int(input("Enter number of students: "))
name=[]
l1=[]
l2=[]
l3=[]
for i in range(0,a):
    student=input("Enter name of student ")
    name.append(student)
    marks=int(input("Enter marks of student  in subject 1 " ))
    l1.append(marks)
    marks=int(input("Enter marks of student  in subject 2 "))
    l2.append(marks)
    marks=int(input("Enter marks of student  in subject 3 "))
    l3.append(marks)
    
print(  name[0],  l1[0],   l2[0],   l3[0])
print(  name[1],  l1[1],   l2[1],   l3[1])    
b=len(l1)
for j in range(0,b):
    if l1[j]<=35:
        print(name[j]," is failed in subject 1")
    if l2[j]<=35:
        print(name[j]," is failed in subject 2")
    if l3[j]<=35:
        print(name[j]," is failed in subject 3")
