list =  [1,2,3,4,5]

# append will add the value in the last 

list.append(6)
print(list)

# sort will arrange the values in the given order
# ascending or descending

list1 = [6,4,5,3,2,1]
list1.sort()    #by default ascending
list1.sort(reverse= True)
print(list1)

a = ['a','c','d','b','e']
# a.sort()
print(a)

# reverse the original list

a.reverse()
print(a)

# insert will add values to specified location or index

list_insert = [6,5,4,3,2,1]
list_insert.insert(0,7)
print(list_insert)

# remove values in the list

list_remove = [1,2,3,4,5,6]
list_remove.remove(2)
print(list_remove)

# pop - it will remove the value based on given index

list_p = [5,4,3,2,1]
list_p.pop(0) # by default it will remove last element
print(list_p)


