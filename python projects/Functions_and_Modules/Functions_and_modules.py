# lambda function
import mymodule
sum = lambda x,y:x+y
print(sum(3,5))
print(sum(8,3))
return_val=lambda x,y,z:x[::-1]+y[::-1]+z[::-1]
print(return_val("aniket ","balasaheb ","kshirsagar "))
print(return_val("rahul ","ritesh ","nimbalkar "))
string=lambda x:[i for i in range(0,x)]
print(string(14))
string=lambda x:[i for i in x]
print(string("Aniket"))
upper=lambda x :x.upper()
print(upper("aniket"))
lower=lambda x :x.lower()
print(lower("ANIKET"))
title=lambda x :x.title()
print(title("aniket balasaheb kshirsagar"))
inagurtion=lambda i :"welcome"
print(inagurtion("a"))
even_no=lambda x :[i for i in range(2,)]
print(mymodule.str)