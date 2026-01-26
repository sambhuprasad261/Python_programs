"""
Variables and Data Types
------------------------
Learn about different data types in Python and how to work with variables.
"""

# Integer (whole numbers)
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Float (decimal numbers)
height = 5.9
print(f"Height: {height}, Type: {type(height)}")

# String (text)
name = "John Doe"
print(f"Name: {name}, Type: {type(name)}")

# Boolean (True/False)
is_student = True
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# Multiple assignment
x, y, z = 10, 20, 30
print(f"\nMultiple assignment: x={x}, y={y}, z={z}")

# Type conversion
num_string = "100"
num_int = int(num_string)
print(f"\nString '{num_string}' converted to integer: {num_int}")

float_num = float(age)
print(f"Integer {age} converted to float: {float_num}")

# String concatenation
first_name = "Jane"
last_name = "Smith"
full_name = first_name + " " + last_name
print(f"\nFull name: {full_name}")

# Getting user input (commented out for automated testing)
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")
