import random 
variable_dict = {}
Cards = ['King', 'Queen' , 'Jack', 10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 ]
value_dict = {"King":10.0, "Queen":10.0, "Jack":10.0}
first_card = random.choice(Cards)
second_card = random.choice(Cards)
dealer_second_card = random.choice(Cards)


print(str(first_card) + " and " + str(second_card))

#Dealer cards
dealer_first_card = random.choice(Cards)
print("The dealer's card is:" + str(dealer_first_card))

#later
next_card = random.choice(Cards)
def extra_card(next_card):
    next_card = random.choice(Cards)
x = 0
while x < 2:
    player_choice = input(str("What do you want to do? Hit or Stand"))
    if player_choice == "Hit":
        extra_card
        print(extra_card)
        x = x+1
    elif player_choice == "Stand":
        print(dealer_second_card)
        if int(dealer_first_card) + int(dealer_second_card) > int(first_card) + int(second_card):
            print("you lost")
        else:
            print("you won") 
    else:
        print("pls repeat")
       

