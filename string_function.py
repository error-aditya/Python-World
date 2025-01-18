str = 'my name is aditya rajput'
# 1
#it will checks it ends with given character and return true or false 
print(str.endswith('ut'))

# 2
# it will capitalize the first letter of the string
print(str.capitalize()) 

# 3
# it will replace the old value with new value
# str(old_value,new_value)

print(str.replace('my','hamara'))

# 4
# find function will search the word inside the string
# if it exists it will return the first index of that word
print(str.find('aditya'))

# 5
# count will count the occurances of the given character
print(str.count('a'))

# practice question
# 1

f_name = input("Enter your first name ->")
print(len(f_name))

# 2

string1 = "$hello $world,$ how a$re y$ou."
print(string1.count('$'))