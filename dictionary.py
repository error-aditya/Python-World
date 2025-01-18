# dictionary uses key-values pair
# mutable can change
# unordered
# don't allow duplicate keys
# keys can be  numbers, strings or floating values

dict = {
    'name': 'Aditya',
    'roll_no': 53,
    'div': 'A',
    'age': 21
}

print(type(dict),dict)
print(dict['name'])

# changing the values for keys
dict['name'] = 'f_name'
print(dict)

# adding new key

dict['surname'] = 'Rajput'
print(dict)

# null dictionary

nul = {}

# nested dictionary

n_dict = {
    'name': 'Aditya',
    'marks' : {
        'maths': 90,
        'science': 80,
        'english': 70
    }
}

print(n_dict['marks'])