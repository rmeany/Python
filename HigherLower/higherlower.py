import random


range = int(input("Please enter a number as your range: "))
random_num = random.randint(1,range)
while True:
    guess = int(input(f"Please guess a number between 1 and {range}: "))
    if guess == random_num:
        print("Congratulations, you guessed right!")
        break
    elif guess < random_num:
        print("Guess was lower, try again...")
    elif guess > random_num:
        print("Guess was higher, try again...")
