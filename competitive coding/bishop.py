from re import A


pos_start=input()
pos_end=input()
bishop_diagonal=[]
pos_x_set=["A","B","C","D","E","F","G","H"]
x1=pos_x_set.index(pos_start[0].upper())+1
y1=int(pos_start[1])
x2=pos_x_set.index(pos_end[0].upper())+1
y2=int(pos_end[1])
print(x1,y1)
print(x2,y2)

def islegal():
    if y2-y1==x2-x1 or y2-y1==-x1+x2:
        return True
    else :
        return False

if islegal():
    print("Yes")
else :
    print("No")


# pos_start=input()
# pos_end=input()
# bishop_diagonal=[]
# pos_x_set=["A","B","C","D","E","F","G","H"]
# sl=pos_x_set.index(pos_start[0].upper())+1
# sn=int(pos_start[1])
# el=pos_x_set.index(pos_end[0].upper())+1
# en=int(pos_end[1])

# rusl=[]
# rusn=[]
# finalRU=[]
    
# if sn <= 8 and sl <= 8 :
#     a=0;
#     while sn<= 8 and sl <= 8 :
#         rusn.append(sn)
#         sn = sn+1;
#         rusl.append(sl)
#         sl = sl+1;
#         a+=1
        
# print(rusn)
# print(rusl)
# print(a)
# for j in range(0,a):
#     finalRU[j].append((rusl[j] * 10) + rusn[j])
    
# endposition = (el*10) + en;
   
# for j in range(0,a):
#     if endposition == finalRU[j]:
#         z=1
        
    
    
# if z==1 :
#     print("Yes");
    
# else:
#     print("No");
    
    
    
    








