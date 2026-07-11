import random

comp_choices = ["rock", "paper", "scissors"]

comp_choice = random.choice(comp_choices)

user_choice1 = input("What do you choose?" \
" Rock " \
"Paper " \
"Or scissors?")
user_choice2 = user_choice1.replace(" ", "")
user_choice =  user_choice2.lower
  
def game(user_choice):
    if comp_choice == "rock":
        if user_choice == "paper":
            print("I chose " + comp_choice, " You win!")
        elif user_choice == "scissors":
            print("I chose " + comp_choice, " you lose!")
        elif user_choice == "rock":
            print("I chose " + comp_choice, " draw!")
    elif comp_choice == "paper":
        if user_choice == "scissors":
            print("I chose " + comp_choice, " You win!")
        elif user_choice == "rock":
            print("I chose " + comp_choice, " you lose!")
        elif user_choice == "paper":
            print("I chose " + comp_choice, " draw!")
    elif comp_choice == "scissors":
        if user_choice == "rock":
            print("I chose " + comp_choice, " You win!")
        elif user_choice == "paper":
            print("I chose " + comp_choice, " you lose!")
        elif user_choice == "scissors":
            print("I chose " + comp_choice, "draw!")
    else:
        print("IDK")

game(user_choice)