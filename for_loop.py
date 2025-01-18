# for loops - they are used to repeat instructions for each item in a list
# it will travel in sequence in lists,strings,tuples

list = [1,2,3,4,5]
tup = (1,2,3,4,5)
str = 'aditya_rajput'

for i in str:
    if i == 'i':
        print('found')
        # break
    print(i)
else: # it is optional
    print('not found')

#  range - it will create a sequence of numbers
# range(start?,stop,step?) ? referes to optional

seq = range(0,10)
for i in seq:
    print(i)


for i in range(1,10,2): # output 1,3,5,7,9
    print(i)

# pass - it will do nothing, it will just pass by continuing the loop

for i in range(10):
    pass

