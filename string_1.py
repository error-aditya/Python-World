# \n it refers to new line
# \t it refers to tab
string1 = 'This is a string.\nMy name is Aditya.'
print(string1)

# Basic operations
# concatenation
a = "My name is "
b = "Aditya_Rajput"
c = a + b 
print("Hello, " + c)

# finding length, it counts space
print(len(c))

'''finding index of a character
we can just access the character using index 
we can't manipulate characters'''

print(string1[0])

# Slicing
# str[starting index : ending index]

print(b[1:3],'\n',b[-7:-1],'\n',b[2:len(b)])
