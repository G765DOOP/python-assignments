# inventory thing for games

inventory = {"nintendo" : 1}

user_does = input("what do you wnat to do?").strip("").lower()



#inventory returner
def add_list():
    if user_gives.lower() in inventory:
        inventory[user_gives] = inventory[user_gives] + 1
    elif user_gives not in inventory:
        print("we dont have that, would u like to donate it?")



#inventory checker
def check_list():
    if user_choice.lower() in inventory:
        inventory[user_choice] = inventory[user_choice] - 1
    elif user_choice not in inventory:
        print("we dont have that")


if user_does == "return":
    user_gives = input("what item u return?")
    add_list()
elif user_does == "check out":
    user_choice = input("which one?").strip(" ").lower()
    check_list()




print(inventory)