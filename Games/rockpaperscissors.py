import random


def latest_score(user_wins, computer_wins):
    return f"User: {user_wins}, Computer: {computer_wins}\n"


num_games = int(input("How many games would you like to play? "))

# Set options
options = ["Rock","Paper","Scissors"]
count = 0
computer_wins = 0
user_wins = 0
user_round_won = True

while count < num_games:
    # Random choice by computer
    computer = options[random.randint(0,2)]
    # User choice
    user = input("Rock, Paper or Scissors? ")

    if user == computer:
        print("Go again")
    else:
        count+=1
        if user == "Rock":
            if computer == "Paper":
                user_round_won = False
                print("Paper beats Rock")
            else:
                print("Rock beats Scissors")
        elif user == "Paper":
            if computer == "Scissors":
                user_round_won = False
                print("Scissors beats Paper")
            else:
                print("Paper beats Rock")
        elif user == "Scissors":
            if computer == "Rock":
                user_round_won = False
                print("Rock beats Scissors")
            else:
                print("Scissors beats Paper")
        else:
            print("I don't know what that was but it wasn't Rock, Paper or Scissors")
        if user_round_won == True:
            user_wins+=1
            print(user_wins)
        else:
            computer_wins+=1

    print("Current score is ", latest_score(user_wins,computer_wins))
