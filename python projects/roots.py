a=int(input("enter a coefficient of x^2 : "))
b=int(input("enter a coefficient of x : "))
c=int(input("enter other nos : "))
if ((b**2)-4*a*c)>0 :
    print("roots are real and unequal ")
    print("1st root is ",((-b+((b**2)-4*a*c)**1/2)/2*a))
    print("1st root is ",((-b-((b**2)-4*a*c)**1/2)/2*a))
elif  ((b**2)-4*a*c)==0 :
    print("roots are real and equal  ")
elif  ((b**2)-4*a*c)<0 :
    print("roots are imaginary ")     