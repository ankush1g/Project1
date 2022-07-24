import random

l=int(input("Enter lower Bound-"))
g=int(input("Enter Upper Bound-"))

x=random.randint(l,g)
print("you are only 7 chance to in this game")

count=0
while count<=7:
    count=count+1
    guess=int(input("guess the number:"))
    if x==guess:
        print("Your guess is correct in ",count,"counts")
        break
    elif x>guess:
        print("Your guess is less than the Number",7-count,"left counts")
    elif x<guess:
        print("your guess is greater than the number",7-count,"left counts")
if count>8:
    print("The number is",x,"this")
    print("Better Luck Next Time")