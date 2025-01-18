# recursion - when a function calls itself repeatedly
# recursion is a kind of version of loops

# recursive function 
def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
    print('end')
show(5)

# call stack - stack of function calls

# recursion through factorial

def fact(n):
    if n == 0 or n == 1:
        return 1
    return fact(n-1) * n
    
print(fact(5))