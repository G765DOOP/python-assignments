# #this is for the uwser's name

# user_name = input("What is your name?")
# vowels = 0
# consonant = 0
# user_name_list = user_name.strip(" ").split(" ")
# spaces = 0
# #how many letters are in the name to check
# # for i in range(len(user_name)):
# #     if user_name_list[i].strip == ' ':


# print(len(user_name_list)-1)



    #     user_name_list.append('*')
    # else:
    #     user_name_list.append(user_name[i])



# # vowels = vowels + 1
# print("".join(user_name_list))


# print(f"there are {vowels} vowels")
#     if user_name[i].lower() in 'bcdfghjklmnpqrstvwxyz':
#         consonant = consonant + 1
    


# print(f"there are {consonant} consonants")



# my_name = "Darsh!"
# print(my_name.isalpha())


# url = "amazon.com/clothes/pants"
# api_endpoint = url.split("/")
# print(api_endpoint[1:])


#input list

# is_palind = True
# for i in range(len(user_word)//2): #racecar
#     if user_word[i] != user_word[-i-1]: #noon
#         print('it is not a palindrome')
#         is_palind = False
#         break


# if is_palind == True:
#     print('it is a palindrome')
# user_word = input('What word do you want to check?')
# l = 0
# r = len(user_word)-1
# while l < r:
#     if user_word[l] != user_word[r]:
#         print('it is not a palindrome')
#         break
#     l+=1
#     r-=1

# if r == len(user_word)//2:
#     print('it is a palindrome')
    
#racec



# biggest_index = 0
# second_biggest = 0
# for i in range(len(userinput)):
#     if userinput[i] > userinput[biggest_index]:
#         second_biggest = biggest_index
#         biggest_index = i

# print(f'the biggest number is {userinput[second_biggest]}')

userinput = [4, 4, 4, 1, 1, 3, 3,1,3,5,2]
unique_elems = set()
dupli_list = []

for i in range(len(userinput)):
    if userinput[i] not in unique_elems:
        unique_elems.add(userinput[i])
    else:
        dupli_list.append(userinput[i])

dupli_list = set(dupli_list)
print(dupli_list)