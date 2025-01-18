# loops - they are used to repeat instructions
# while loops - they are used to repeat instructions while a certain condition is met


# while loop
# when condition will be false then it goes out of loop
# print numbers 5 to 1
i =  5      # iterator
while i >=1 :    # iteration
    print('hello',i)
    i -= 1

# break - it will break or terminate where 'break' is written

# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1

# continue - terminates execution in the current iteration & 
# continues of the loop with the next iteration

i = 1
while i <= 10:
    if(i % 2 == 0):
        i += 1
        continue # it will skip 3 and print 1,2,4,5
    print(i)
    i += 1