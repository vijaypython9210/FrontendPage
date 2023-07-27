import random

target=random.randint(1,50)
n=int(input("Can you guess the number what im think? "))

while(n!=target):
    if(n<target):
        print("target Number is greater than Your guessing number")
    else:
        print("target number is smaller than your guessing number")
    print("Guess Again")
    n=int(input("Enter a number: "))
print("You are Won!")
