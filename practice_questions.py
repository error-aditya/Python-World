# practice question
'''
# 1 - WAP to ask user to enter names of his 3 favorite movies and stores in a list

a = input("Enter your favorite movie1 name ->")
b = input("Enter your favorite movie2 name ->")
c = input("Enter your favorite movie3 name ->")
d = [a,b,c]
print(d,'\n',type(d))

# we could have use append
# d.append(a), d.append(b),d.append(c)

# 2 - WAP to check if a list contains a palindrome of elements.

list = [1,2,3,2,1]
if list == list[::-1]:
    print("Its a palindrome")
else:
    print("Its not a palindrome")

# we can use copy for finding palindrome

l = list.copy()
l.reverse()
if list == l:
    print("Its a palindrome")
else:
    print("Its not a palindrome")

# 3 - WAP to count the students with grade A

grade = ('C','D','A','A','B','B','A')
print(grade.count('A'))

# 4 - Store above values in the list and sort a to d

list1 = list(grade)  # we have converted the tuple into list
list1.sort()
print(list1,'\n',type(list1))


# 5 - store these word meanings in a python dictionary

dict = {}
dict.update({'table': ['a piece of furniture','list of facts & figures'],'cat': 'a small aanimal'})
print(dict)

# 6 - you are given a list of subjects for the students. 
# Assume one classroom is required for 1 subject.
# how many classrooms are needed by all students

sub1 = {'python','java','C++','python','javascript'}
sub2 = {'java','python','java','C++','C'}

classroom = sub1.union(sub2)
print(len(classroom), 'classrooms are needed for the students.')


# 7 - WAP to enter marks of 3 subjects from user and store them in a dictionary. 
# start with an empty dictionary & add one by one.
# use subject name as key & marks as value

dict = {}
# dict.update({'subject': {'maths': 90,'science': 80, 'english' : 70}})
dict['maths'] = 90
dict['science'] = 80
dict['english'] = 70
print(dict)

# 8 - figure out a way to store 9 & 9.0 as separate values in the set.
# (you can take help of built-in-functions)

set1 = {9,'9.0',('float',9.0,9),('int',9,9.0)}
print(type(set1),set1)


# 9 - print numbers from 1 to 100

num = 1
while num <= 100:
    print(num)
    num += 1

# 10 - print numbers from 100 to 1

nums = 100
while nums >= 1:
    print(nums)
    nums -= 1

# 11 - print multiplication table of a number n

n = 5
num = 1

while num <= 10:
    nums = n * num
    print(n,'x',num,'=',nums)
    num +=1
while num <= 10:
    print(5 *num)
    num += 1

# 12 - print the elements of the following list using a loop

n = 1
while n <=10:
    num = n * n 
    print(num)
    n += 1


# 13 - search for a number x in this tuple using loop

tup = (1,4,9,16,25,36,49,64,81,100)
n = 36

while n in tup:
    print('The number is there in this tuple')
else:
    print('The number is not there in this tuple')
    
# 14 - print the elements of the following list using a loop

list = [1,4,9,16,25,36,49,64,81,100]
ip = []

for i in list:
    ip.append(i)
    print(ip,type(ip))
print(ip)

num = 10
for i in range(1,10):
    if i <= num:
        print(i * i)
        i += 1

# 15 - search a number x in this tuple using loop

tup = (1,4,9,16,25,36,49,64,81,100)
# x = 100
# idx = 0
for i in tup:
    i = int(input("Enter a number ->"))
    if i in tup:
        print("The number is in tuple at index")
    # idx += 1
    else:
        print("The number is not in tuple")
    break
    

# 16 - print numbers from 1 to 100

for i in range(1,101):
    print(i)

# 17 - print numbers from 100 to 1

for i in range(100,0,-1):
    print(i)

# 18 - print multiplication table of a number n
n = 6
for i in range(11):
    # i = int(input('Enter a number ->'))
    print(n,'x',i,'=',n * i)

# 19 - WAP to find the sum of first n natural numbers using whule

a = 1
sum = 0
while a <= 7:
    sum += a
    a += 1
print(sum)
    
# 20 - WAP to find the factorial of first n numbers

fact = 1
for i in range(1,6):
    # fact = i
    fact *= i
    i += 1
print(fact)
    
i = 1
fact = 1
while i <= 5:
    print(i)
    fact *= i
    i += 1   
print(fact)

# 21 - WAP to print the length of a list

def length(list = [1,2,3,4,5]):
    list1 = []
    list1 = list.copy()
    print(len(list),list,type(list),type(list1))
print(length([1,2,3]))

# 22 - WAF to print the elements of a list in a single line.

def print_list(list = [1,2,3,4,5]):
    list1 = []
    list1 = list.copy()
    print(list1,type(list1))
print(print_list([5,4,3,2,1]))

# 23 - WAF to find the factorial of n.

def f(n):
    fact = 1
    for i in range(1,n):
        fact *= i
        print(fact)

f(7)

# 24 - WAF to convert USD to INR

def con_usd_to_inr(usd):
    inr = usd * 80
    print('The amount in INR us ->',inr)
con_usd_to_inr(int(input('Enter the amount in USD -> ')))

# 25 - takes a input if its odd or even returms 'odd' or 'even' in string

def str_odd_even(num):
    if num % 2 == 0:
        print('The number is even')
    else:
        print('The number is odd')
str_odd_even(int(input('Enter the number -> ')))

# 26 - write a recursive function to calculate the sum of first n natural numbers

def r_sum(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num + r_sum(num - 1)

print(r_sum(int(input('Enter the number ->'))))

# 27 - write a recursive function to print all elements in a list.

def r_list(list,idx = 0):
    if idx == len(list):
        return
    else:
        print(list[idx])
        r_list(list,idx + 1)
print(r_list([1,2,3]))

'''