import random

a=1
b=6
name=input("enter your name")
count=0
while count<=7:
    count=count+1
    x=random.randint(a,b)
    yes=int(input("you want to roll the dice 0 or 1: "))
    if yes==1:
        y=random.randint(a,b)
        if x==y:
            print("Computer and you Draw the match")
            print("Computer:",x,name,':',y)
        elif x>y:
            print("Computer Won the match")
            print("Computer:",x,name,":",y)
        elif x<y:
            print("You Won the match Computer lose the match")
            print("Computer:",x,name,":",y)

    else:
        print("Choose the 1 to play the Dice Game:")
        break
        

