# Simple addition
def add(a, b):
    return a + b

# Simple subtraction
def subtract(a, b):
    return a - b

# Simple multiplication
def multiply(a, b):
    return a * b

# Simple division
def divide(a, b):
    return a / b

# Get the numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add/subtract/multiply/divide): ")

# Run the right calculation based on what user picked
if operation == "add":
    print(f"Result: {add(num1, num2)}")
elif operation == "subtract":
    print(f"Result: {subtract(num1, num2)}")
elif operation == "multiply":
    print(f"Result: {multiply(num1, num2)}")
elif operation == "divide":
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid operation")
