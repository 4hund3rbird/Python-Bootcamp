n=input()
s=0
for i in n:
    s+=pow(int(i),len(n))

if s==int(n):
    print("Armstrong")
else:
    print("Not Armstrong")