#__________________________________
#	project:	rps_v4.py
#	author:		Adam
#	date:		20170104
#	purpose:        Rock, Paper, Scissors
#                       demonstrates use of Python List,
#                       generates a random number to select a list item
#                       allows human player to type move (R, P, S)
#                       demonstrates use of if/elif to
#                       compare player moves and determine a winner
#       reference:      https://docs.python.org/3.5/library/random.html#random.randint
#
#__________________________________

from random import randint
 
#create a list of play options "Rock", "Paper", "Scissors"
smoothMoves = ["r", "p", "s"]

#create variables for keeping track of the score
scoreHuman = 0
scoreComputer = 0

#assign a random moves to the computer
computer = smoothMoves[randint(0,2)]

#create variable for human player moves
human = ""

#create while loop to continue playing game
while (True):
    #create test to determine score/winner/exit
    if (scoreHuman >=3):
        print("_________________________________________")
        print("")
        print("  The human wins Master of the Universe. ")
        print("")
        print("_________________________________________")
        print("")
        print("Type 'new game' to play again. \ntype 'exit' to exit.\n")
        newGame = input()
        if newGame == "new game":
            scoreHuman = 0
            scoreComputer = 0
            continue
        if newGame == "exit":
            break

    if (scoreComputer >=3):
        print("_________________________________________")
        print("")
        print("  The computer wins Master of the Universe. ")
        print("")
        print("_________________________________________")
        print("")
        print("Type 'new game' to play again. \ntype 'exit' to exit.\n")
        newGame = input()
        if newGame == "new game":
            scoreHuman = 0
            scoreComputer = 0
            continue
        if newGame == "exit":
            break

    print ("Human, it is your move... ")     
    human = input("Type 'r', 'p', or 's':   ")
    
    #create test to determine which move is a winner
    if human == computer:
        print("Tie!")
    elif human == "r":
        if computer == "p":
            print("")
            print("You lose!", computer, "covers", human)       #computer wins
            print("")
            scoreComputer = scoreComputer + 1
        else:
            print("You win!", human, "smashes", computer)       #human wins
            scoreHuman = scoreHuman + 1
    elif human == "p":
        if computer == "s":
            print("You lose!", computer, "cut", human)          #computer wins
            scoreComputer = scoreComputer + 1
        else:
            print("You win!", human, "covers", computer)        #human wins
            scoreHuman = scoreHuman + 1
    elif human == "s":
        if computer == "r":
            print("You lose...", computer, "smashes", human)    #computer wins
            scoreComputer = scoreComputer + 1
        else:
            print("You win!", human, "cut", computer)           #human wins
            scoreHuman = scoreHuman + 1
    else:
        print("That's not a valid play. Check your spelling!")

    #display scores and allow computer to choose a move
    print("Human score: " + str(int(scoreHuman)))
    print("Computer score: " + str(int(scoreComputer)))
    print("")
    computer = smoothMoves[randint(0,2)]
