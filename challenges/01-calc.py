# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print('What calculation would you like to do? (add, sub, mult, div)')

while True:
    choice = input("Enter choice: ")

    if choice in ('add', 'sub', 'mult', 'div'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'add':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'sub':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'mult':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'div':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
