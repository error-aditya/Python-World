try:
    x = int(input('Enter a value -> '))
    print(x)
except ValueError:
    print('Value is not integer..write integer')
finally:
    print('Try except finished')