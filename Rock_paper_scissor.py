import random

name = "Daniel"

element = ["rock", "paper", "scissor"]
computer_choice = random.choice(element)

user_choice = input("Enter rock, paper or scissor choice = ")
C = computer_choice
U = user_choice

while C == U:
    print("Draw")
    break

while C != U:
    if C == "rock" and U == "paper":
        print(F"{name} won")
    elif C == "rock" and U == "scissor":
        print("Computer won")
    elif C == "paper" and U == "scissor":
        print(F"{name} won")
    elif C == "paper" and U == "rock":
        print("Computer won")
    elif C == "scissor" and U == "rock":
        print(F"{name} won")
    elif C == "scissor" and U == "paper":
        print("Computer won")
    else:
        print("Check the option or spelling of your choice!!!")
    break


