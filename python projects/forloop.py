a=int(input("num 1 : "))
b=int(input("num 2 : "))
c=int(input("num 3 : "))
if a!=b and b!=c :
    if a>b:
        if  a>c :
            print (a," is the greatest !")        
    elif b>c:
        print(b,"  is the greatest !")
    else :
        print(c," is the greatest !") 
elif a==b and b!=c:
    print(max(b,c),"is the greatest !")  
elif b==c and b!=a:
    print(max(a,b),"is the greatest")                 
else :
    print("You have entered same nos!!")        