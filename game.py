# game.py

print("Welcome to my Rock-Paper-Scissors Game")



Choice = input("Please choose either 'Rock', 'Paper', or 'Scissors':")


list = ["Rock", "Paper", "Scissors"]
while Choice not in list:
    Choice = input("Please try again. Choose either 'Rock', 'Paper', or 'Scissors':")
else:
    print('You chose', Choice)    


import random # load the module to avoid `NameError: name 'random' is not defined`

Computer = random.choice(list)
print('The Computer Chose',Computer)

Tie = "You and the Computer tied."
Win = "You win!"
Lose = "The Computer wins.  Better luck next time."

if Choice is "Rock" and Computer is "Rock":
    print(Tie)
elif Choice is "Rock" and Computer is "Paper":
    print(Lose)
elif Choice is "Rock" and Computer is "Scissors":
    print(Win)
elif Choice is "Paper" and Computer is "Rock":
    print(Win)
elif Choice is "Paper" and Computer is "Paper":
    print(Tie)
elif Choice is "Paper" and Computer is "Scissors":
    print(Lose)
elif Choice is "Scissors" and Computer is "Rock":
    print(Lose)
elif Choice is "Scissors" and Computer is "Scissors":
    print(Tie)
else:
    print(Win)

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