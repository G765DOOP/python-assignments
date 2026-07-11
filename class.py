user_name = input("What is your name?")
vowel = 0
for index in range(len(user_name)):
    if user_name[index].lower() in 'aeiou':
        vowel = vowel+1

print(f"there are {vowel} vowels in the name {user_name}" )



# '''if user_guess%3 == 0 and user_guess%5 == 0:
#     print("fizzbuzz")
# elif user_guess%5 == 0:
#     print("buzz")
# elif user_guess%3 == 0:
#     print("Fizz")
# else:
#     print("neither")'''