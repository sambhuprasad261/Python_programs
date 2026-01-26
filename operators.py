"""
Operators in Python
------------------
Learn about arithmetic, comparison, and logical operators.
"""

print("=" * 50)
print("ARITHMETIC OPERATORS")
print("=" * 50)

# Basic arithmetic
a = 10
b = 3

print(f"a = {a}, b = {b}\n")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

print("\n" + "=" * 50)
print("COMPARISON OPERATORS")
print("=" * 50)

x = 5
y = 8

print(f"x = {x}, y = {y}\n")
print(f"Equal to (x == y): {x == y}")
print(f"Not equal to (x != y): {x != y}")
print(f"Greater than (x > y): {x > y}")
print(f"Less than (x < y): {x < y}")
print(f"Greater than or equal (x >= y): {x >= y}")
print(f"Less than or equal (x <= y): {x <= y}")

print("\n" + "=" * 50)
print("LOGICAL OPERATORS")
print("=" * 50)

p = True
q = False

print(f"p = {p}, q = {q}\n")
print(f"AND (p and q): {p and q}")
print(f"OR (p or q): {p or q}")
print(f"NOT (!p): {not p}")

# Practical example
age = 20
has_license = True

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE")
print("=" * 50)
print(f"Age: {age}, Has License: {has_license}")
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")
