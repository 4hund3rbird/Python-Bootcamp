# *
import winsound
import time
n=int(input())

for i in range(n):
    winsound.beep(1) 
    for j in range(n):
        time.sleep(0.003)
        if(j<((n/2)-i)) or (j>(n/2)+i):
            print(" ",end="")
        elif i>=int(n/2) and (j>n-int(n/4) or j<int(n/4)):
            print(" ",end="")
        else:
            print("*",end="")
    print()