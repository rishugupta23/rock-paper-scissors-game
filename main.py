'''
rock = 1
paper = 2
scissors = 3
'''
import random
computer = random.choice([1,2,3])
you=input("enter your choice = ")   # user will insert r for rock,p for paper and s for scissor
gamedict={"r":1,"p":2,"s":3}
youfinal=gamedict[you]
reversegamedict={1:"rock",2:"paper",3:"scissor"}

print(f"You chosen {reversegamedict[youfinal]}\nComputer chosen {reversegamedict[computer]}")

if(computer == youfinal):
    print("its a draw")
else:
    if( computer == 1 and youfinal == 2):
        print("You win!")
    elif( computer == 1 and youfinal == 3):
        print("You lose!")
    elif( computer == 2 and youfinal == 1):
        print("You lose!")
    elif( computer == 2 and youfinal == 3):
        print("You win!")
    elif( computer == 3 and youfinal == 1):
        print("You win!")
    elif( computer == 3 and youfinal == 2):
        print("You lose!")
