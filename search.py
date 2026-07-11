list = [1, 2, 3, 5, 9, 10, 11, 13, 15]
user_want = int(input("What number are you looking for?"))
for i in range(len(list)):
    if user_want == list[i]:
        print(f"{user_want} is in {i+1}")
    elif user_want == list[i]:
        i = i + 1
