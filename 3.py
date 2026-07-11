import random
#player betting
bet_amount = input("Enter bet amount:")
bet_amount = int(bet_amount)
#Gambling house
percent = [1.5, 1.1, 1, 0.9, 0.8, 0.7, 0.5, 0]
random_win_percent = random.choice(percent)
print("now you have " + str((random_win_percent)*bet_amount) + " dollars")
