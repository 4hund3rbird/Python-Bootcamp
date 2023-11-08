s=input()
ispallendrome=True
for i in range(int(len(s)/2)):
    if(s[i]!=s[len(s)-i-1]):
        ispallendrome=False
        break

if ispallendrome:
    print("pallendrome")
else:
    print("not pallendrome")