import os
from random import randint

password = input("Enter the password->")

keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        "1","2","3","4","5","6","7","8","9","0"
        ]

pwg = ""

while(pwg!=password):
    pwg=""
    for i in range(len(password)):
        guesspass = keys[randint(0,35)]
        pwg = str(guesspass)+str(pwg)
        print(pwg)
        print("Vaar lage,Aem no thay rekha!")
        os.system("cls")

print(f"The Password is -> {pwg}")
