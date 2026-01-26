"""
Conditional Statements
---------------------
Learn about if, elif, and else statements for decision making.
"""

print("=" * 50)
print("SIMPLE IF-ELSE")
print("=" * 50)

# Simple if-else
temperature = 25

if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant.")

print("\n" + "=" * 50)
print("IF-ELIF-ELSE")
print("=" * 50)

# Multiple conditions with elif
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

print("\n" + "=" * 50)
print("NESTED CONDITIONS")
print("=" * 50)

# Nested if statements
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter the venue.")
    else:
        print("You need an ID to enter.")
else:
    print("You must be 18 or older to enter.")

print("\n" + "=" * 50)
print("LOGICAL OPERATORS IN CONDITIONS")
print("=" * 50)

# Using logical operators
username = "admin"
password = "pass123"

if username == "admin" and password == "pass123":
    print("Login successful!")
else:
    print("Invalid credentials.")

# Checking multiple conditions
number = 15

if number > 0 and number % 2 == 0:
    print(f"{number} is a positive even number")
elif number > 0 and number % 2 != 0:
    print(f"{number} is a positive odd number")
else:
    print(f"{number} is not a positive number")

print("\n" + "=" * 50)
print("TERNARY OPERATOR")
print("=" * 50)

# Ternary operator (short form)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")
