string="EIQQEIOEEEIOAAOAIAEIEAQQEEIIEIAIQQOOQOEIEOEAAIIQIAAOQEEIOIAAEAOEEAOQAOAOEAAQIIEAOIOOOQQAEEOEOEOIEEAQAEIAIAEIOEQEIEOEAAOAIIQEQOIEEAIOIQEQIEAQOAQOEIOEOOIIOOAQQEOQQQEQOIQEOAOOIQAIEIOIOEQAOQAIIOIIOAIEQOOIQIIAQAAAQOOOOOQQOQOAEEOIEEEOEQAEEQAOQQAIEAIEIQQOQIEAQOOQEIQIIEQIQOAEIQOOEEEAAOOIIQAOIQAOEAEIIIQEQQAIEOEEQIOIEQIAIIOIOQEQQIIIQAAOAOIOQIQQOOAOIOOAOIEIIEIEIIIQQIEIQEQEEEOEQOAAAIEEAAOEEIQIIAQIQIAQQEIOOAQAEAEOEAOEQAEEQEAAAOOIQIEEIOOOAQEEOQEQOAQOIAOOAOAIIQIOQOIEEIEIEOOEQQEAEOIQOAAAEIQEQAOEOEOOQAEOQOIEQEQEAAOOAQAQEEQAOIEOQAOOAIAEOIOAAIQAOIEEOQOAIEAOEEQQQEEOIAEOQAOEAQAOEIIAEQAAIIEQAEQQOOAIIAAOEQAQQIAIOAIAOIEAIQAOAAAIEQQEEOAQQIQOQQQAOIIOAEIOIIOOIIIAEIEOQOEOIOQQEAIEIOOIOAAEOOEIIAEOEOQIAIOEEIQAIOEQEIIEEQAEAQAOOAAEEAOOIQOAAAIAIQQEOQAEIIIAEAQEAOQOEEIIIAIQEOIOOIIQAIIQAOAQIQEAQIQOAEEAAOAIIEOQAIQIAQEOIIEAAAAIOEAOIIIQQEEIEQQIIIQIQIOAOIQIQAIAOQEIQEQEEOIEEAIEQIQAOAEQAQEOAQOQQEEEOQAIOOQQOEEQQOOIEAAOAOAAEAOQQIOAOOEEIAAQIQAQOOIOOIEIQIEIEQEIEEIAQIEAIIIIIIEEEOQOEOIQAIAAIOOQQEEQOIQOAEAAEAOIAEIAOEIOOEOIIEIAEQIOAEEQQOQEOEIOIAAIQAOEAIEIEIEA"
# Stuart 406312
vowels=["A","E","I","O","U"]
sub=[]
stuart_substrings=[]
kevin_substrings=[]
# k=1
# strlist=[i for i in string]
# for j in range(0,len(string)):
#     for i in range(0,len(string)):
       
#         m=i
#         n=i+k
#         if n<= len(string):
#             sub.append(strlist[m:n])
#         elif n>len(string):
#             continue    
#     k+=1



stu_score=0
kev_score=0    
s=string
n=len(s)    
for i in range(n):
    temp=""
    for j in range(i,n):
        temp+=s[j]
        sub.append(temp)
        a=temp
        if a[0] in vowels :
            if a not in kevin_substrings:
                kevin_substrings.append(a)
            elif a in kevin_substrings:
                kev_score+=1    
        else :
            if a not in stuart_substrings:
                stuart_substrings.append(a)
            elif a in stuart_substrings:
                stu_score+=1     

# for i in range(0,len(sub)):
#     a=sub[i]
#     if a[0] in vowels :
#         if a not in kevin_substrings:
#             kevin_substrings.append(a)
#     else :
#         if a not in stuart_substrings:
#             stuart_substrings.append(a)
        
# stuart_substringsdup=[]
# for i in stuart_substrings:
#     if i not in stuart_substringsdup:
#         stuart_substringsdup.append(i) 

     
  

# kevin_substringsdup=[]
# for i in kevin_substrings:
#     if i not in kevin_substringsdup:
#         kevin_substringsdup.append(i) 

kev_score+=len(kevin_substrings)
stu_score+=len(stuart_substrings)

# for j in kevin_substrings:
#     c=sub.count(j)
#     kev_score+=c
  
# for i in stuart_substrings:
#     c=sub.count(i)
#     stu_score+=c
    

if stu_score>kev_score:
    print("Stuart",stu_score) 
elif kev_score>stu_score:
    print("Kevin",kev_score)
else:
    print("Draw")           
        