user_list = [1,5,4,3,3,2,5,8,7,9,9]
new_list = set()

for i in range(len(user_list)):
    if user_list[i] not in new_list:
        new_list.add(user_list[i])

print(new_list)
