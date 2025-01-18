# # 1) simple program to replace the words
# input1 = input('Entre your sentence -> ')
# print(input1)
# word1 = input('Enter a word to replace -> ')
# word2= input('Enter a word to replace with that word -> ')
# print(input1.replace(word1,word2))

# 2) simple calculator

input1 = int(input('Enter First Number -> '))
input2 = int(input('Enter Second Number -> '))

def calculator(input3):
    match input3:
        case '+':
            return input1 + input2
        case '*':
            return input1 * input2
        case '/':
            return input1 / input2
        case '-':
            return input1 - input2
        case default:
            return 'Invalid Operation'

sums = calculator(input('Enter the operation -> '))
print(sums)