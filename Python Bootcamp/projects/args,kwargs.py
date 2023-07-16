
# *args is an argument which will tell compiler that this function can have unlimited positional arguments

from urllib3 import add_stderr_logger


def add(*args):
    total=0
    # print(args) # args saves all the positional arguments in a tuple
    for i in args: # we can loop through args
        total+=i
    print(total)


def calculations(n,**kwargs):
    n+=kwargs.get("add") 
    n-=kwargs.get("sub")
    n*=kwargs.get("mul")
    n/=kwargs.get("div")
    print(n)

calculations(10,add=10,mul=20,sub=5,div=2)