"""
Functions in Python
------------------
Learn how to define and use functions.
"""

print("=" * 50)
print("SIMPLE FUNCTION")
print("=" * 50)

# Simple function without parameters
def greet():
    """Print a greeting message."""
    print("Hello! Welcome to Python functions.")

greet()

print("\n" + "=" * 50)
print("FUNCTION WITH PARAMETERS")
print("=" * 50)

# Function with parameters
def greet_person(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

print("\n" + "=" * 50)
print("FUNCTION WITH RETURN VALUE")
print("=" * 50)

# Function with return value
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

print("\n" + "=" * 50)
print("FUNCTION WITH DEFAULT PARAMETERS")
print("=" * 50)

# Function with default parameter
def power(base, exponent=2):
    """Calculate power of a number (default exponent is 2)."""
    return base ** exponent

print(f"2^2 = {power(2)}")
print(f"2^3 = {power(2, 3)}")

print("\n" + "=" * 50)
print("FUNCTION WITH MULTIPLE RETURN VALUES")
print("=" * 50)

# Function returning multiple values
def get_stats(numbers):
    """Return min, max, and sum of a list."""
    return min(numbers), max(numbers), sum(numbers)

nums = [1, 5, 3, 9, 2]
minimum, maximum, total = get_stats(nums)
print(f"Numbers: {nums}")
print(f"Min: {minimum}, Max: {maximum}, Sum: {total}")

print("\n" + "=" * 50)
print("FUNCTION WITH VARIABLE ARGUMENTS")
print("=" * 50)

# Function with *args (variable number of arguments)
def calculate_sum(*numbers):
    """Calculate sum of any number of arguments."""
    return sum(numbers)

print(f"Sum of 1, 2, 3: {calculate_sum(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {calculate_sum(1, 2, 3, 4, 5)}")

print("\n" + "=" * 50)
print("FUNCTION WITH KEYWORD ARGUMENTS")
print("=" * 50)

# Function with **kwargs (keyword arguments)
def print_info(**info):
    """Print information from keyword arguments."""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="New York")

print("\n" + "=" * 50)
print("RECURSIVE FUNCTION")
print("=" * 50)

# Recursive function - factorial
def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

print("\n" + "=" * 50)
print("LAMBDA FUNCTION")
print("=" * 50)

# Lambda function (anonymous function)
square = lambda x: x ** 2
print(f"Square of 7: {square(7)}")

# Lambda with multiple parameters
multiply = lambda x, y: x * y
print(f"5 * 6 = {multiply(5, 6)}")
