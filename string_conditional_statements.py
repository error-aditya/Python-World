# conditional statements
# 1
# if-elif-else(SYNTAX)

'''age = int(input("Enter your age - > "))

if(age >= 18):
    print("He can apply for driving licence") #indentation  
elif(age == 16):
    print("He can apply for learner's licence")
else:
    print("He is not eligible for having driving licence")
'''


# 2
# nesting - if inside if

'''age = int(input("Enter your age - > "))

if(age >= 18):
    if(age >= 80):                                 # nested if
        print('You are a senior citizen')
    else:
        print("He can apply for driving licence") #indentation 
elif(age == 16):
    print("He can apply for learner's licence")
else:
    print("He is not eligible for having driving licence")
'''

# practice question
# 1

marks = int(input("Enter your marks ->"))

if(marks >= 90):
    print("Grade A")
elif(marks >= 80 and marks < 90):
    print("Grade B")
elif(marks >=70 and marks < 80):
    print("Grade C")
elif(marks < 70):
    print("Grade D")
else:
    print("Invalid marks")

# 2

num = int(input("Enter a number ->"))

if(num % 2 == 0):
    print('The number is Even')
elif(num % 2 != 0):
    print('The number is odd')
else:
    print('Invalid number')

# 3

a = int(input('Enter first number -> ')) 
b = int(input('Enter second number -> '))
c = int(input('Enter third number -> '))

if(a > b and a > c):
    print('A is greater than b and c.')
elif(b > a and b > c):
    print('B is greater than a and c.')
else:
    print('C is greater than a and b.')

# 4

num = int(input('Enter a number ->'))

if(num % 7 == 0):
    print('The number is multiple of 7')
else:
    print('The number is not multiple of 7')