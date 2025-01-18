# # function - a block of code that performs a specific task
# # deccrease redundancies

# # __l__ is dunder function
# def __hello__():
#     print("hello")
# __hello__()

# # simple function
# def add(a,b):       # a,b are parameters 
#     return a + b

# print(add(10,15))       # 10,15 are arguments 

# # average of 3 numbers

# def average():
#     a1 = int(input("Enter first number ->"))
#     b1 = int(input("Enter second number ->"))
#     c1 = int(input("Enter third number ->"))
#     sum = a1 + b1 + c1
#     avg = sum / 3
#     return avg

# print(average())

# # * helps to print more values and type will be tuple
# def greetings(*names):
#     print('Welcome',names[0],type(names))

# greetings('Aditya','Aman','Ridhhi')

for i in range(5,0,-1):
    num = 0
    for j in range(num,i + 1):
        num = num + 1
        print(num,end=' ')
    print('')