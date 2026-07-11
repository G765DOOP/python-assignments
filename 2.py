# n = 0
# while n <5 :
#     n = n+1
#     print(n)

#for loop 
#array
# fruits = ["apple", "banana", "cherry"] 
# for x in fruits:
#   print(x)


# n = [1, 2, 3, 4, 5]
# for number in range(6): 
#   print(number)


# def myint(x,y):
#         s = x+y 
#         return s


# b = myint(2,3)
# print(b)


x = int(input("What would you like the factorial of?"))

def fact(x):
        y = x
        while(x>1):
                y = y*(x-1)
                x = x -1
        print(y)
fact(x)