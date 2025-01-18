# list - it stores multiple values inside a single list

marks =  [90,80,70,60,50]
print(marks)
print(type(marks))
print(marks[2])

# in python we can store different types of values in single list
# strings are immutable 
# lists are mutable
 
marks[2] = 81
print(marks)

# list Sclicing - we can get sub list
# list[starting_index:ending_index]

print(marks[1:4],'\n',marks[-3:])