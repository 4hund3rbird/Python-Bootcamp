# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# 200
n_shoes=int(input())
n_size=list(input().split())
n_cust=int(input())
cust_size=[]
cust_cost=[]
profit=0
for i in range(0,n_cust) :
    size,cost =input().split()
    cust_size.append(size)
    cust_cost.append(cost)
print(cust_size)
print(cust_cost)
print(n_size)
for i in n_size:
    a=cust_size.count(i)
    b=n_size.count(i)
    if a == b :
        pass
        
            
          
        
            
    