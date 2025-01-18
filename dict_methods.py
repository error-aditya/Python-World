dict = {
    'name' : 'Aditya',
    'div' : 'A',
    'roll_no' : 53,
    'age' : 21,
    'degree' : 'mca',
    'sports' : {
        'cricket' : 'good',
        'football' : 'good',
        'badmintion' : 'average',
        'vollyball' : 'good'
    }
}

# print(dict)

# it will returns all keys in a list

print(dict.keys())

# it will return all values in a list

print(dict.values())

# it will return in tuple, 
# so we can access using index

a = dict.items()
print(type(a))

# get will return the value of the given key

print(dict['sports'])  # if we write[sports1] it will give -> error

# if error comes then it will be stopped and after the error the code won't execute 
# we can use get() to avoid this error
print(dict.get('sports')) # if we write [sports1] it will give -> none


# update will add the key values pair into the old dictionary

dict.update({'city': 'ahmedabad'})
print(dict)