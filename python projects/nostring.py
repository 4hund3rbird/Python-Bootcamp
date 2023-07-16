mc="AAAABCBBABAAACKGGGGFIJK"
# mc=input()
arr=[]
k=list(mc)
for i in range(0,len(k)-1):
    a=[]
    for j in range(i+1,len(k)):
        if k[i]==k[j]:
            a.append(k[j])
            arr.append(a)
            break
        else:
            break
print(arr)            
    
        
            
   
      
# print(k)

# for i in range(0,len(k)):
#     count=0
#     for j in range(i,len(k)):
#         if k[j]==k[j+1]
#             count+=1
#     print(k[j],count)    
    
    
    
    
    # for j in mc:
    #     if i==j :
    #         count+=1