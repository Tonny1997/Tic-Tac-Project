#You an also also CMD
from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer

computer = t[randint(0,2)]

#Make the player to False
player = False

while player == False:
#Now set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print(" This a Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You have lost!", computer, "covers", player)
        else:
            print("You have won!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You have now  lost!", computer, "cut", player)
        else:
            print("You won!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
