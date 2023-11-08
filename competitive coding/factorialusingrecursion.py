def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)

def fibonnaci(n):
    if(n==0):
        return 1
    print(n)
    return fibonnaci()
print(factorial(5))