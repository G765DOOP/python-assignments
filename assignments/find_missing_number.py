'''input = [1,2,3,5,6,7]
output = 4
approach #1:
make a new list based off of the length of the original list
check what is the difference between the lists'''

# ordered_input = set(user_input)
# for i in range(len(user_input)+1):
#     if i+1 not in ordered_input:
#         print(i+1)
'''approach #2:
add all the numbers in the user_input then subtract it from the value it should be'''
user_input = [1,5,7,6,2,3,4]
user_sum = 0
for i in range(len(user_input)):
    user_sum = user_input[i]+ user_sum

n = len(user_input)+1
print(user_sum)
print(n)
print(((n*(n+1))/2)-user_sum)
