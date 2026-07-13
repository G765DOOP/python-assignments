''' 
input = "banana"
output = ban

turn it into an array
make a new set to track unique letters
add the unique letters into another list
and then return it as a string'''

user_input = 'banana'
unique_characters = set()
result_list = []

for i in range(len(user_input)):
    if user_input[i] not in unique_characters:
        result_list.append(user_input[i])
        unique_characters.add(user_input[i])


print(''.join(result_list))