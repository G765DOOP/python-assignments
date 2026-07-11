
def num(x, y):

    operation = input("What do you want to do with those number?")
    if operation == "+":
     print( x + y )
    elif operation == "-":
       print(x-y)
    elif operation == "/":
       print(x/y)
    elif operation == "*":
       print(x*y)
   

x = int(input("What is your first number?"))
y = int(input("What is your second number?"))

num(x,y)


