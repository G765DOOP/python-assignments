user_word = input('What word do you want to check?')
l = 0
r = len(user_word)-1
while l < r:
    if user_word[l] != user_word[r]:
        print('it is not a palindrome')
        break
    l+=1
    r-=1

if r == len(user_word)//2:
    print('it is a palindrome')