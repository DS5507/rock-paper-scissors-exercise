# game.py

import random # load the module to avoid `NameError: name 'random' is not defined`

print("Welcome to my Rock-Paper-Scissors Game")
print("----------------------------------------------")
# Capture Inputs

Choice = input("Please choose either 'Rock', 'Paper', or 'Scissors':")

# Validate Input

list = ["Rock", "Paper", "Scissors"]
while Choice not in list:
    Choice = input("Invalid selection, please try again. Choose either 'Rock', 'Paper', or 'Scissors':")
else:
    print('You chose', Choice)    

# Generate Computer Selection

Computer = random.choice(list)
print('The Computer Chose',Computer)

# Determine the Winner
# Display Final Outcome

Tie = "You and the Computer tied."
Win = "You win!"
Lose = "The Computer wins.  Better luck next time."

if Choice == Computer:
    print(Tie)
elif Choice == "Rock" and Computer == "Paper":
    print(Lose)
elif Choice == "Rock" and Computer == "Scissors":
    print(Win)
elif Choice == "Paper" and Computer == "Rock":
    print(Win)
elif Choice == "Paper" and Computer == "Scissors":
    print(Lose)
elif Choice == "Scissors" and Computer == "Rock":
    print(Lose)
elif Choice == "Scissors" and Computer == "Paper":
    print(Win)
else:
    pass


print('Thanks for playing.  Please play again!')


#
#Play_Again = ['Y', 'N', 'Yes', 'No']
#Play_Now = input('Would you like to play again now? (Y/N):')
#while Play_Now not in Play_Again:
#    Play_Now = input('Would you like to play again now? (Y/N):')
#else:
#    if Play_Now is 'Y' or 'Yes':
#        XXX
#    else:
#        exit()