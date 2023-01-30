import random

# Need to track number of user and computer wins.
user_wins = 0
computer_wins = 0

# List to contain number of options.
options = ["rock", "paper", "scissors"]

# Create loop to check user input
while True:
    # Get user input and check if it's valid
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

