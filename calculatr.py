# program for a simple calculator
import math
# a function that adds two numbers
def add(x, y):
    return x + y

# a function that subtracts two numbers
def subtract(x, y):
    return x - y

# a function that multiplies two numbers
def multiply(x, y):
    return x * y

# a function that divides two numbers
def divide(x, y):
    return x / y
# a function that finds the square root of X (X>0)
def square_root(x):
   return  math.sqrt(x)

print("Choose operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.SquareRoot")
while True:
    # takes input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice == '5':
        x =float(input("Enter the number to find square root:"))
        print("Square Root of",x,"is",square_root(x))

    elif choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break