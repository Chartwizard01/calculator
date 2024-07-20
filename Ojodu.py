print("Welcome to Hardman arithmetic solution \n Please select an arithmetic operation from the options below to proceed")

operation = input("+ or - or * or / or ") 

num1 = float(input("enter an integer: "))

num2 = float(input("enter an integer: "))

if operation == "+":
    print(num1 + num2)

if operation == "-":
    print(num1 - num2)

if operation == "*":
    print(num1 * num2)

if operation == "/":
    print(num1 / num2)


else:
    print("Invalid operation")