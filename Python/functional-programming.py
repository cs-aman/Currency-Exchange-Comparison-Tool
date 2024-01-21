from functools import reduce

# Define higher-order functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

# Function to perform an operation on a list using a higher-order function
def operate_on_list(numbers, operation):
    return reduce(operation, numbers)

# Example of using the functional calculator

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use higher-order functions and functional programming principles
result_addition = operate_on_list(numbers, add)
result_multiplication = operate_on_list(numbers, multiply)

# Display the results
print(f"Addition result: {result_addition}")
print(f"Multiplication result: {result_multiplication}")
