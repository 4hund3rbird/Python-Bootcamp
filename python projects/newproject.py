l1=[1,2,3]
lx=[]
ly=[]
lz=[]
for i in range(0,l1[0]+1):
    lx.append(i)
print(lx) 
for i in range(0,l1[1]+1):
    ly.append(i)
print(ly)
for i in range(0,l1[2]+1):
    lz.append(i)
print(lz)           
count=0
coord=[]
for x in range(0,len(lx)):
    for y in range(0,len(ly)):
        for z in range(0,len(lz)):
            print(lx[x],ly[y],lz[z])
            cod=[]
            cod.append(lx[x])
            cod.append(ly[y])
            cod.append(lz[z])
            coord.append(cod)
            count+=1
print(count)  
print(coord)          